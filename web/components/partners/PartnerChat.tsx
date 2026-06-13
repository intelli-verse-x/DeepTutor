"use client";

/**
 * Web chat with a partner over `WS /api/v1/partners/{id}/ws`.
 *
 * The socket forwards every chat-loop StreamEvent verbatim (`stream_event`
 * frames carry the backend event's `to_dict()`, which IS the frontend
 * `StreamEvent` shape), so this reuses product chat's rendering wholesale:
 * `AssistantActivity` shows the live thinking/tool trace (open while
 * working, collapsed once answered) and the answer text is recomputed with
 * the same narration-demotion rules as chat.
 */

import { useCallback, useEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import dynamic from "next/dynamic";
import { Paperclip } from "lucide-react";
import { wsUrl } from "@/lib/api";
import { getPartnerHistory } from "@/lib/partners-api";
import type { ExportableMessage } from "@/lib/chat-export";
import type { StreamEvent } from "@/lib/unified-ws";
import { docIconFor, formatBytes, isSvgFilename } from "@/lib/doc-attachments";
import {
  isNarrationMarker,
  recomputeAnswerContent,
  shouldAppendEventContent,
} from "@/lib/stream";
import { AssistantActivity } from "@/components/chat/home/TracePanels";
import {
  PartnerComposer,
  type PartnerPendingAttachment,
} from "@/components/partners/PartnerComposer";
import PartnerAvatar from "@/components/partners/PartnerAvatar";

const AssistantResponse = dynamic(
  () => import("@/components/common/AssistantResponse"),
  { ssr: false },
);

interface ChatMsg {
  role: "user" | "assistant";
  content: string;
  attachments?: PartnerMessageAttachment[];
  /** Full turn event stream (live turns only; restored history has none). */
  events?: StreamEvent[];
  error?: boolean;
}

interface PartnerMessageAttachment {
  type: string;
  filename: string;
  mimeType?: string;
  size?: number;
  previewUrl?: string;
}

function resetsVisibleConversation(content: string) {
  const command = content.trim().split(/\s+/, 1)[0]?.toLowerCase();
  return command === "/new" || command === "/clear";
}

function normalizeHistoryAttachments(
  value: unknown,
): PartnerMessageAttachment[] {
  if (!Array.isArray(value)) return [];
  return value
    .map((item): PartnerMessageAttachment | null => {
      if (!item || typeof item !== "object") return null;
      const obj = item as Record<string, unknown>;
      const filename = String(obj.filename || "");
      if (!filename) return null;
      const sizeRaw = obj.size;
      return {
        type: String(obj.type || "file"),
        filename,
        mimeType: String(obj.mime_type || obj.mimeType || ""),
        size: typeof sizeRaw === "number" ? sizeRaw : undefined,
      };
    })
    .filter((item): item is PartnerMessageAttachment => item !== null);
}

function sentAttachmentsForMessage(
  attachments: PartnerPendingAttachment[],
): PartnerMessageAttachment[] {
  return attachments.map((item) => ({
    type: item.type,
    filename: item.filename,
    mimeType: item.mimeType,
    size: item.size,
    previewUrl: item.previewUrl,
  }));
}

function AttachmentStrip({
  attachments,
}: {
  attachments?: PartnerMessageAttachment[];
}) {
  if (!attachments?.length) return null;
  return (
    <div className="mt-2 flex flex-wrap gap-1.5">
      {attachments.map((attachment, index) => {
        if (
          (attachment.type === "image" || isSvgFilename(attachment.filename)) &&
          attachment.previewUrl
        ) {
          return (
            <div
              key={`${attachment.filename}-${index}`}
              className="h-14 w-14 overflow-hidden rounded-lg border border-[var(--border)] bg-[var(--muted)]/35"
              title={attachment.filename}
            >
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={attachment.previewUrl}
                alt={attachment.filename}
                className={`h-full w-full ${isSvgFilename(attachment.filename) ? "object-contain p-1" : "object-cover"}`}
              />
            </div>
          );
        }

        const spec = docIconFor(attachment.filename);
        const Icon = spec.Icon;
        const sizeLabel = attachment.size ? formatBytes(attachment.size) : "";
        return (
          <div
            key={`${attachment.filename}-${index}`}
            className="flex max-w-[190px] items-center gap-2 rounded-lg border border-[var(--border)] bg-[var(--card)]/80 px-2 py-1.5"
            title={attachment.filename}
          >
            <div className="flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-[var(--muted)]/60">
              {attachment.filename ? (
                <Icon size={15} strokeWidth={1.5} className={spec.tint} />
              ) : (
                <Paperclip className="h-3.5 w-3.5 text-[var(--muted-foreground)]" />
              )}
            </div>
            <div className="min-w-0 flex-1">
              <div className="truncate text-[11px] font-medium text-[var(--foreground)]">
                {attachment.filename}
              </div>
              <div className="truncate text-[9px] uppercase text-[var(--muted-foreground)]">
                {sizeLabel ? `${spec.label} · ${sizeLabel}` : spec.label}
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default function PartnerChat({
  partnerId,
  partnerName,
  emoji,
  color,
  avatar,
  onMessagesChange,
}: {
  partnerId: string;
  partnerName: string;
  emoji?: string;
  color?: string;
  avatar?: string;
  /** Lifts the settled conversation up so the page header can export it.
   *  Fires only on discrete message events (send / turn done / clear), not
   *  per streamed token — the live `draft` is intentionally excluded. */
  onMessagesChange?: (messages: ExportableMessage[]) => void;
}) {
  const { t } = useTranslation();
  const [messages, setMessages] = useState<ChatMsg[]>([]);
  const [streaming, setStreaming] = useState(false);
  const [connected, setConnected] = useState(false);
  // Live turn snapshot for rendering. The authoritative accumulator is a
  // local variable inside the socket effect (event handlers may mutate it
  // freely); every frame publishes a fresh snapshot object here.
  const [draft, setDraft] = useState<{
    events: StreamEvent[];
    content: string;
  } | null>(null);
  const wsRef = useRef<WebSocket | null>(null);
  const scrollRef = useRef<HTMLDivElement | null>(null);
  const sessionIdRef = useRef<string>("");

  useEffect(() => {
    if (!sessionIdRef.current) {
      sessionIdRef.current = `web-${Math.random().toString(36).slice(2, 10)}`;
    }
  }, []);

  const scrollToBottom = useCallback((behavior: ScrollBehavior = "smooth") => {
    requestAnimationFrame(() => {
      scrollRef.current?.scrollTo({
        top: scrollRef.current.scrollHeight,
        behavior,
      });
    });
  }, []);

  // Restore recent history (all sessions merged → the partner's memory feel).
  useEffect(() => {
    let cancelled = false;
    void getPartnerHistory(partnerId, { limit: 60 })
      .then((history) => {
        if (cancelled) return;
        setMessages(
          history
            .filter((m) => m.role === "user" || m.role === "assistant")
            .map((m) => ({
              role: m.role as "user" | "assistant",
              content: m.content,
              attachments: normalizeHistoryAttachments(
                (m as Record<string, unknown>).attachments,
              ),
            })),
        );
        requestAnimationFrame(() => scrollToBottom("instant"));
      })
      .catch(() => {});
    return () => {
      cancelled = true;
    };
  }, [partnerId, scrollToBottom]);

  useEffect(() => {
    const ws = new WebSocket(wsUrl(`/api/v1/partners/${partnerId}/ws`));
    wsRef.current = ws;
    ws.onopen = () => setConnected(true);

    // Authoritative live-turn accumulator. Lives in the effect scope so
    // socket handlers can mutate it cheaply; renders see snapshots only.
    let live: { events: StreamEvent[]; content: string } | null = null;
    const publish = () => {
      setDraft(
        live ? { events: [...live.events], content: live.content } : null,
      );
    };

    ws.onmessage = (e) => {
      const data = JSON.parse(e.data) as {
        type: string;
        content?: string;
        event?: StreamEvent;
      };
      if (data.type === "stream_event" && data.event) {
        const event = data.event;
        live ??= { events: [], content: "" };
        live.events.push(event);
        if (shouldAppendEventContent(event)) {
          live.content += event.content;
        } else if (isNarrationMarker(event)) {
          // A round resolved as narration — its streamed text belongs to
          // the trace, not the answer. Same demotion rule as product chat.
          live.content = recomputeAnswerContent(live.events);
        }
        publish();
        scrollToBottom();
      } else if (data.type === "content") {
        // Authoritative final text from the runner (covers terminator /
        // ask_user fallbacks the client-side recompute can't know about).
        const finished = live;
        live = null;
        setMessages((msgs) => [
          ...msgs,
          {
            role: "assistant",
            content: data.content || finished?.content || "",
            events: finished?.events.length ? finished.events : undefined,
          },
        ]);
        publish();
        scrollToBottom();
      } else if (data.type === "done") {
        setStreaming(false);
        live = null;
        publish();
      } else if (data.type === "proactive") {
        setMessages((msgs) => [
          ...msgs,
          { role: "assistant", content: data.content ?? "" },
        ]);
        scrollToBottom();
      } else if (data.type === "error") {
        setMessages((msgs) => [
          ...msgs,
          { role: "assistant", content: data.content ?? "Error", error: true },
        ]);
        live = null;
        publish();
        setStreaming(false);
      }
    };

    ws.onclose = () => {
      setConnected(false);
      setStreaming(false);
    };

    return () => {
      ws.close();
      wsRef.current = null;
    };
  }, [partnerId, scrollToBottom]);

  // Report the settled transcript to the parent for header export controls.
  useEffect(() => {
    onMessagesChange?.(
      messages.map((msg) => ({
        role: msg.role,
        content: msg.content,
        attachments: msg.attachments?.map((a) => ({
          type: a.type,
          filename: a.filename,
          mime_type: a.mimeType,
        })),
      })),
    );
  }, [messages, onMessagesChange]);

  const handleSend = useCallback(
    (content: string, attachments: PartnerPendingAttachment[]) => {
      if (
        streaming ||
        !wsRef.current ||
        wsRef.current.readyState !== WebSocket.OPEN
      )
        return;
      const visibleContent =
        content ||
        (attachments.every((item) => item.type === "image")
          ? t("Please analyze the attached image(s).")
          : t("Please use the attached file(s)."));
      wsRef.current.send(
        JSON.stringify({
          content: visibleContent,
          session_id: sessionIdRef.current,
          attachments: attachments.map((item) => ({
            type: item.type,
            filename: item.filename,
            base64: item.base64,
            mime_type: item.mimeType,
          })),
        }),
      );
      if (resetsVisibleConversation(visibleContent)) {
        setMessages([]);
      } else {
        setMessages((msgs) => [
          ...msgs,
          {
            role: "user",
            content: visibleContent,
            attachments: sentAttachmentsForMessage(attachments),
          },
        ]);
      }
      setDraft({ events: [], content: "" });
      setStreaming(true);
      scrollToBottom();
    },
    [streaming, scrollToBottom, t],
  );

  return (
    <div className="flex h-full min-h-0 flex-col">
      <div ref={scrollRef} className="min-h-0 flex-1 overflow-y-auto px-1 py-4">
        {messages.length === 0 && !draft ? (
          <div className="flex h-full flex-col items-center justify-center gap-3 text-center">
            <PartnerAvatar
              name={partnerName}
              emoji={emoji}
              color={color}
              image={avatar}
              size={56}
            />
            <div>
              <p className="text-[15px] font-medium text-[var(--foreground)]">
                {partnerName}
              </p>
              <p className="mt-1 max-w-sm text-[12.5px] text-[var(--muted-foreground)]">
                {t(
                  "Say hello — this conversation shares the same memory your partner has on its connected channels.",
                )}
              </p>
            </div>
          </div>
        ) : (
          <div className="mx-auto flex max-w-2xl flex-col gap-5">
            {messages.map((msg, i) =>
              msg.role === "user" ? (
                <div key={i} className="flex justify-end">
                  <div className="max-w-[75%] rounded-2xl bg-[var(--secondary)] px-4 py-2.5 text-[14px] leading-relaxed text-[var(--foreground)] shadow-sm">
                    {msg.content ? (
                      <div className="whitespace-pre-wrap">{msg.content}</div>
                    ) : null}
                    <AttachmentStrip attachments={msg.attachments} />
                  </div>
                </div>
              ) : (
                <div key={i} className="flex items-start gap-2.5">
                  <PartnerAvatar
                    name={partnerName}
                    emoji={emoji}
                    color={color}
                    size={26}
                  />
                  <div className="min-w-0 flex-1">
                    {msg.events && msg.events.length > 0 && (
                      <AssistantActivity
                        events={msg.events}
                        isStreaming={false}
                        content={msg.content}
                        className="mb-1.5"
                        agentName={partnerName}
                        showMark={false}
                        headerClassName="min-h-[26px]"
                      />
                    )}
                    {msg.error ? (
                      <p className="text-[13px] text-[var(--destructive)]">
                        {msg.content}
                      </p>
                    ) : (
                      <AssistantResponse content={msg.content} />
                    )}
                  </div>
                </div>
              ),
            )}

            {draft && (
              <div className="flex items-start gap-2.5">
                <PartnerAvatar
                  name={partnerName}
                  emoji={emoji}
                  color={color}
                  size={26}
                />
                <div className="min-w-0 flex-1">
                  <AssistantActivity
                    events={draft.events}
                    isStreaming
                    content={draft.content}
                    className="mb-1.5"
                    agentName={partnerName}
                    showMark={false}
                    headerClassName="min-h-[26px]"
                  />
                  {draft.content ? (
                    <AssistantResponse content={draft.content} />
                  ) : null}
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      <div className="mx-auto w-full max-w-2xl px-1 pb-4">
        {!connected && (
          <p className="mb-1 text-center text-[11px] text-[var(--muted-foreground)]">
            {t("Connecting…")}
          </p>
        )}
        <PartnerComposer
          onSend={handleSend}
          disabled={streaming || !connected}
        />
      </div>
    </div>
  );
}
