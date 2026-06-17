"use client";

import { useEffect, useMemo, useState } from "react";
import {
  ArrowLeft,
  Bot,
  CalendarDays,
  Check,
  ChevronDown,
  ChevronRight,
  Eye,
  FolderOpen,
  Loader2,
  Minus,
  Search,
} from "lucide-react";
import { useTranslation } from "react-i18next";
import PickerShell from "@/components/common/PickerShell";
import PickerHeader from "@/components/common/PickerHeader";
import type { SelectedHistorySession } from "@/components/chat/HistorySessionPicker";
import { listImportedSessions } from "@/lib/imports-api";
import {
  getSession,
  type SessionDetail,
  type SessionSummary,
} from "@/lib/session-api";
import {
  epochMsToISODate,
  projectLabel,
  SOURCE_LABEL,
  type ImportSource,
} from "@/lib/chat-import";
import { getAgents, type ImportAgent } from "@/lib/chat-import/agent-store";
import {
  assignSessionsToAgents,
  readImportMeta,
} from "@/lib/chat-import/attribution";
import { normalizeMessageContent, truncateText } from "@/lib/message-content";

interface MyAgentsPickerProps {
  open: boolean;
  onClose: () => void;
  onApply: (sessions: SelectedHistorySession[]) => void;
}

const UNGROUPED_PREFIX = "ungrouped:";
const ALL = "__all__";

interface SubGroup {
  key: string;
  label: string;
  kind: "project" | "date";
  sessions: SessionSummary[];
  latest: number;
}

function formatDay(key: string, lang: string): string {
  const d = new Date(`${key}T00:00:00`);
  if (Number.isNaN(d.getTime())) return key;
  return d.toLocaleDateString(lang, {
    year: "numeric",
    month: "short",
    day: "numeric",
    weekday: "short",
  });
}

/**
 * Reference picker for imported agent conversations. Conversations are stored
 * as normal sessions, so a selection is just a list of session ids — the same
 * shape and backend path as the Chat History reference. Here we attribute each
 * conversation to its named agent (via the IndexedDB registry), let the user
 * filter by agent, then organize that agent's conversations by project (Claude
 * Code) or day (Codex) so they can pick a whole group or individual chats.
 */
export default function MyAgentsPicker({
  open,
  onClose,
  onApply,
}: MyAgentsPickerProps) {
  const { t, i18n } = useTranslation();
  const [sessions, setSessions] = useState<SessionSummary[]>([]);
  const [agents, setAgents] = useState<ImportAgent[]>([]);
  const [selectedIds, setSelectedIds] = useState<string[]>([]);
  const [query, setQuery] = useState("");
  const [activeAgent, setActiveAgent] = useState<string>(ALL);
  const [expanded, setExpanded] = useState<Set<string>>(new Set());
  const [loading, setLoading] = useState(false);
  const [preview, setPreview] = useState<{
    session: SessionSummary;
    detail: SessionDetail | null;
    loading: boolean;
  } | null>(null);

  useEffect(() => {
    if (!open) return;
    let mounted = true;
    const load = async () => {
      setLoading(true);
      try {
        const [data, reg] = await Promise.all([
          listImportedSessions(200, 0, { force: true }),
          getAgents(),
        ]);
        if (!mounted) return;
        setSessions(data);
        setAgents(reg);
      } catch {
        if (mounted) {
          setSessions([]);
          setAgents([]);
        }
      } finally {
        if (mounted) setLoading(false);
      }
    };
    void load();
    return () => {
      mounted = false;
    };
  }, [open]);

  // Reset transient state each time the picker opens.
  useEffect(() => {
    if (open) {
      setQuery("");
      setActiveAgent(ALL);
      setSelectedIds([]);
      setExpanded(new Set());
      setPreview(null);
    }
  }, [open]);

  // Owner key per session: the agent id, or an ungrouped-by-source bucket.
  const ownerKeyById = useMemo(() => {
    const ordered = [...agents].sort(
      (a, b) => (b.lastSyncAt || b.createdAt) - (a.lastSyncAt || a.createdAt),
    );
    const owner = assignSessionsToAgents(sessions, ordered);
    const map = new Map<string, string>();
    for (const session of sessions) {
      const meta = readImportMeta(session);
      if (!meta) continue;
      const sid = session.session_id || session.id;
      map.set(sid, owner.get(sid) ?? `${UNGROUPED_PREFIX}${meta.source}`);
    }
    return map;
  }, [agents, sessions]);

  const labelForKey = useMemo(() => {
    const byId = new Map(agents.map((a) => [a.id, a.name]));
    return (key: string): string => {
      if (key.startsWith(UNGROUPED_PREFIX)) {
        const src = key.slice(UNGROUPED_PREFIX.length) as ImportSource;
        return SOURCE_LABEL[src] ?? src;
      }
      return byId.get(key) ?? t("Untitled conversation");
    };
  }, [agents, t]);

  // Filter chips — every owner that has at least one conversation, ordered with
  // named agents first (registry order), then ungrouped source buckets.
  const chips = useMemo(() => {
    const counts = new Map<string, number>();
    for (const key of ownerKeyById.values())
      counts.set(key, (counts.get(key) ?? 0) + 1);
    const ordered = [...agents]
      .sort(
        (a, b) => (b.lastSyncAt || b.createdAt) - (a.lastSyncAt || a.createdAt),
      )
      .map((a) => a.id)
      .filter((id) => counts.has(id));
    const ungrouped = [...counts.keys()]
      .filter((k) => k.startsWith(UNGROUPED_PREFIX))
      .sort();
    return [...ordered, ...ungrouped].map((key) => ({
      key,
      label: labelForKey(key),
      count: counts.get(key) ?? 0,
    }));
  }, [agents, ownerKeyById, labelForKey]);

  // Group the (chip- and search-filtered) sessions by project (Claude Code) or
  // day (Codex), so the user can bulk-pick a project/day or drill in.
  const groups = useMemo<SubGroup[]>(() => {
    const keyword = query.trim().toLowerCase();
    const map = new Map<string, SubGroup>();
    for (const session of sessions) {
      const sid = session.session_id || session.id;
      const ownerKey = ownerKeyById.get(sid);
      if (!ownerKey) continue;
      if (activeAgent !== ALL && ownerKey !== activeAgent) continue;
      if (keyword) {
        const title = String(session.title || "").toLowerCase();
        const last = normalizeMessageContent(
          session.last_message,
        ).toLowerCase();
        if (!title.includes(keyword) && !last.includes(keyword)) continue;
      }
      const meta = readImportMeta(session);
      if (!meta) continue;
      const isCodex = meta.source === "codex";
      const unit = isCodex
        ? epochMsToISODate(session.created_at * 1000)
        : meta.sourceCwd;
      const key = `${meta.source}:${unit}`;
      const group =
        map.get(key) ??
        ({
          key,
          kind: isCodex ? "date" : "project",
          label: isCodex ? formatDay(unit, i18n.language) : projectLabel(unit),
          sessions: [],
          latest: 0,
        } satisfies SubGroup);
      group.sessions.push(session);
      group.latest = Math.max(group.latest, session.updated_at);
      map.set(key, group);
    }
    return Array.from(map.values()).sort((a, b) => b.latest - a.latest);
  }, [sessions, ownerKeyById, activeAgent, query, i18n.language]);

  const toggleSession = (id: string) =>
    setSelectedIds((prev) =>
      prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id],
    );

  const toggleGroup = (group: SubGroup) => {
    const ids = group.sessions.map((s) => s.session_id || s.id);
    setSelectedIds((prev) => {
      const all = ids.every((id) => prev.includes(id));
      if (all) return prev.filter((id) => !ids.includes(id));
      const set = new Set(prev);
      ids.forEach((id) => set.add(id));
      return [...set];
    });
  };

  const toggleExpand = (key: string) =>
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(key)) next.delete(key);
      else next.add(key);
      return next;
    });

  const openPreview = async (session: SessionSummary) => {
    const sid = session.session_id || session.id;
    setPreview({ session, detail: null, loading: true });
    try {
      const detail = await getSession(sid);
      // Ignore if the user navigated away from this preview meanwhile.
      setPreview((cur) =>
        cur && (cur.session.session_id || cur.session.id) === sid
          ? { ...cur, detail, loading: false }
          : cur,
      );
    } catch {
      setPreview((cur) =>
        cur && (cur.session.session_id || cur.session.id) === sid
          ? { ...cur, loading: false }
          : cur,
      );
    }
  };

  const handleApply = () => {
    const selected = sessions
      .filter((session) =>
        selectedIds.includes(session.session_id || session.id),
      )
      .map((session) => ({
        sessionId: session.session_id || session.id,
        title: session.title || t("Untitled conversation"),
      }));
    onApply(selected);
    onClose();
  };

  // When searching, reveal every group so matches aren't hidden behind a
  // collapsed header.
  const searching = query.trim().length > 0;

  return (
    <PickerShell
      open={open}
      onClose={onClose}
      labelledBy="agents-picker-title"
      className="p-4 backdrop-blur-md"
      backdropClass="bg-[var(--background)]/65"
    >
      <div className="w-[min(48rem,92vw)] overflow-hidden rounded-2xl border border-[var(--border)] bg-[var(--card)] text-[var(--card-foreground)] shadow-[0_18px_56px_rgba(0,0,0,0.16)]">
        <PickerHeader
          icon={Bot}
          titleId="agents-picker-title"
          title={t("Select agent conversations")}
          subtitle={t(
            "Pick an agent, then choose the conversations to bring in.",
          )}
          onClose={onClose}
        />

        <div className="bg-[var(--background)]/40 p-5">
          {/* Agent filter chips */}
          {chips.length > 0 && (
            <div className="mb-3 flex flex-wrap items-center gap-1.5">
              <Chip
                label={t("All")}
                active={activeAgent === ALL}
                onClick={() => setActiveAgent(ALL)}
              />
              {chips.map((chip) => (
                <Chip
                  key={chip.key}
                  label={chip.label}
                  count={chip.count}
                  active={activeAgent === chip.key}
                  onClick={() => setActiveAgent(chip.key)}
                />
              ))}
            </div>
          )}

          <div className="mb-4 flex items-center gap-2">
            <div className="relative flex-1">
              <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[var(--muted-foreground)]" />
              <input
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                placeholder={t("Search conversations by title or last message")}
                className="w-full rounded-xl border border-[var(--border)] bg-[var(--card)] py-2.5 pl-9 pr-3 text-[13px] text-[var(--foreground)] outline-none transition focus:border-[var(--primary)]/50 focus:ring-2 focus:ring-[var(--primary)]/15"
              />
            </div>
            <button
              onClick={() => setSelectedIds([])}
              disabled={!selectedIds.length}
              className="rounded-xl border border-[var(--border)] bg-[var(--card)] px-3 py-2.5 text-[12px] font-medium text-[var(--muted-foreground)] transition-colors hover:bg-[var(--muted)] hover:text-[var(--foreground)] disabled:opacity-40"
            >
              {t("Clear")}
            </button>
          </div>

          <div className="max-h-[56vh] overflow-y-auto rounded-2xl border border-[var(--border)] bg-[var(--card)]">
            {preview ? (
              <PreviewPane
                preview={preview}
                selected={selectedIds.includes(
                  preview.session.session_id || preview.session.id,
                )}
                onBack={() => setPreview(null)}
                onToggleSelect={() =>
                  toggleSession(
                    preview.session.session_id || preview.session.id,
                  )
                }
              />
            ) : loading ? (
              <div className="flex min-h-[280px] items-center justify-center">
                <Loader2 className="h-5 w-5 animate-spin text-[var(--muted-foreground)]" />
              </div>
            ) : groups.length ? (
              <div
                key={activeAgent}
                className="animate-fade-in divide-y divide-[var(--border)]"
              >
                {groups.map((group) => {
                  const ids = group.sessions.map((s) => s.session_id || s.id);
                  const selectedInGroup = ids.filter((id) =>
                    selectedIds.includes(id),
                  ).length;
                  const checkState =
                    selectedInGroup === 0
                      ? "none"
                      : selectedInGroup === ids.length
                        ? "all"
                        : "some";
                  const isOpen = searching || expanded.has(group.key);
                  const GroupIcon =
                    group.kind === "date" ? CalendarDays : FolderOpen;
                  return (
                    <div key={group.key}>
                      <div className="sticky top-0 z-10 flex items-center gap-2.5 border-b border-[var(--border)] bg-[var(--card)]/95 px-4 py-2.5 backdrop-blur">
                        <TriCheck
                          state={checkState}
                          onClick={() => toggleGroup(group)}
                          label={t("Select")}
                        />
                        <button
                          type="button"
                          onClick={() => toggleExpand(group.key)}
                          className="flex min-w-0 flex-1 items-center gap-2 text-left"
                        >
                          {isOpen ? (
                            <ChevronDown
                              size={14}
                              className="shrink-0 text-[var(--muted-foreground)]"
                            />
                          ) : (
                            <ChevronRight
                              size={14}
                              className="shrink-0 text-[var(--muted-foreground)]"
                            />
                          )}
                          <GroupIcon
                            size={14}
                            className="shrink-0 text-[var(--muted-foreground)]"
                          />
                          <span className="truncate text-[12.5px] font-semibold text-[var(--foreground)]">
                            {group.label}
                          </span>
                        </button>
                        <span className="shrink-0 text-[11px] text-[var(--muted-foreground)]">
                          {selectedInGroup > 0
                            ? `${selectedInGroup}/${ids.length}`
                            : t("{{count}} chats", { count: ids.length })}
                        </span>
                      </div>

                      {isOpen && (
                        <div className="divide-y divide-[var(--border)]">
                          {group.sessions.map((session) => {
                            const id = session.session_id || session.id;
                            const selected = selectedIds.includes(id);
                            return (
                              <div
                                key={id}
                                className={`group/row flex w-full items-start transition-colors ${
                                  selected
                                    ? "bg-[var(--primary)]/[0.08]"
                                    : "hover:bg-[var(--muted)]/40"
                                }`}
                              >
                                <button
                                  type="button"
                                  onClick={() => toggleSession(id)}
                                  className="flex min-w-0 flex-1 items-start gap-3 py-3 pl-10 pr-2 text-left"
                                >
                                  <div
                                    className={`mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-md border transition-all ${
                                      selected
                                        ? "scale-105 border-[var(--primary)] bg-[var(--primary)] text-[var(--primary-foreground)]"
                                        : "border-[var(--border)] text-transparent"
                                    }`}
                                  >
                                    <Check size={12} />
                                  </div>
                                  <div className="min-w-0 flex-1">
                                    <span className="block truncate text-[14px] font-medium text-[var(--foreground)]">
                                      {session.title ||
                                        t("Untitled conversation")}
                                    </span>
                                    {session.last_message ? (
                                      <p className="mt-1 line-clamp-2 text-[12px] leading-5 text-[var(--muted-foreground)]">
                                        {truncateText(
                                          normalizeMessageContent(
                                            session.last_message,
                                          ),
                                          200,
                                        )}
                                      </p>
                                    ) : null}
                                    <div className="mt-2 text-[11px] text-[var(--muted-foreground)]/85">
                                      {session.message_count ?? 0}{" "}
                                      {t("messages")}
                                    </div>
                                  </div>
                                </button>
                                <button
                                  type="button"
                                  onClick={() => void openPreview(session)}
                                  title={t("Preview")}
                                  aria-label={t("Preview")}
                                  className="mr-3 mt-3 shrink-0 rounded-lg border border-transparent p-1.5 text-[var(--muted-foreground)] opacity-0 transition-all hover:border-[var(--border)] hover:text-[var(--foreground)] focus:opacity-100 group-hover/row:opacity-100"
                                >
                                  <Eye size={15} />
                                </button>
                              </div>
                            );
                          })}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            ) : (
              <div className="px-6 py-14 text-center text-[13px] text-[var(--muted-foreground)]">
                {t("No imported conversations found.")}
              </div>
            )}
          </div>

          <div className="mt-4 flex items-center justify-between gap-3">
            <div className="text-[12px] text-[var(--muted-foreground)]">
              {selectedIds.length === 1
                ? t("1 conversation selected")
                : t("{{n}} conversations selected", { n: selectedIds.length })}
            </div>
            <button
              onClick={handleApply}
              disabled={!selectedIds.length}
              className="btn-primary rounded-xl bg-[var(--primary)] px-4 py-2.5 text-[13px] font-medium text-[var(--primary-foreground)] transition-opacity hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-40"
            >
              {t("Use Selected ({{n}})", { n: selectedIds.length })}
            </button>
          </div>
        </div>
      </div>
    </PickerShell>
  );
}

function TriCheck({
  state,
  onClick,
  label,
}: {
  state: "none" | "some" | "all";
  onClick: () => void;
  label: string;
}) {
  return (
    <button
      type="button"
      onClick={(e) => {
        e.stopPropagation();
        onClick();
      }}
      aria-label={label}
      className={`flex h-4 w-4 shrink-0 items-center justify-center rounded border transition-colors ${
        state === "none"
          ? "border-[var(--border)] bg-transparent hover:border-[var(--primary)]/60"
          : "border-[var(--primary)] bg-[var(--primary)] text-[var(--primary-foreground)]"
      }`}
    >
      {state === "all" ? (
        <Check size={11} strokeWidth={3} />
      ) : state === "some" ? (
        <Minus size={11} strokeWidth={3} />
      ) : null}
    </button>
  );
}

function PreviewPane({
  preview,
  selected,
  onBack,
  onToggleSelect,
}: {
  preview: {
    session: SessionSummary;
    detail: SessionDetail | null;
    loading: boolean;
  };
  selected: boolean;
  onBack: () => void;
  onToggleSelect: () => void;
}) {
  const { t } = useTranslation();
  const { session, detail, loading } = preview;
  const messages = (detail?.messages ?? []).filter(
    (m) => (m.content || "").trim() && m.role !== "system",
  );
  return (
    <div className="animate-fade-in">
      <div className="sticky top-0 z-10 flex items-center gap-2 border-b border-[var(--border)] bg-[var(--card)]/95 px-3 py-2.5 backdrop-blur">
        <button
          type="button"
          onClick={onBack}
          aria-label={t("Back")}
          className="shrink-0 rounded-lg p-1.5 text-[var(--muted-foreground)] transition-colors hover:bg-[var(--muted)] hover:text-[var(--foreground)]"
        >
          <ArrowLeft size={16} />
        </button>
        <div className="min-w-0 flex-1">
          <div className="truncate text-[13px] font-semibold text-[var(--foreground)]">
            {session.title || t("Untitled conversation")}
          </div>
          <div className="text-[11px] text-[var(--muted-foreground)]">
            {session.message_count ?? messages.length} {t("messages")}
          </div>
        </div>
        <button
          type="button"
          onClick={onToggleSelect}
          className={`inline-flex shrink-0 items-center gap-1.5 rounded-lg border px-2.5 py-1.5 text-[12px] font-medium transition-colors ${
            selected
              ? "border-[var(--primary)] bg-[var(--primary)] text-[var(--primary-foreground)]"
              : "border-[var(--border)] text-[var(--muted-foreground)] hover:text-[var(--foreground)]"
          }`}
        >
          {selected ? <Check size={13} /> : null}
          {selected ? t("Selected") : t("Select")}
        </button>
      </div>

      {loading ? (
        <div className="flex min-h-[280px] items-center justify-center">
          <Loader2 className="h-5 w-5 animate-spin text-[var(--muted-foreground)]" />
        </div>
      ) : messages.length ? (
        <div className="space-y-3 px-4 py-4">
          {messages.map((m) => (
            <div key={m.id}>
              <div className="mb-1 text-[10px] font-semibold uppercase tracking-[0.1em] text-[var(--muted-foreground)]">
                {m.role === "user" ? t("You") : t("Assistant")}
              </div>
              <div className="whitespace-pre-wrap break-words rounded-xl border border-[var(--border)]/60 bg-[var(--background)]/40 px-3 py-2 text-[12.5px] leading-relaxed text-[var(--foreground)]">
                {m.content}
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="px-6 py-14 text-center text-[13px] text-[var(--muted-foreground)]">
          {t("This conversation has no readable messages.")}
        </div>
      )}
    </div>
  );
}

function Chip({
  label,
  count,
  active,
  onClick,
}: {
  label: string;
  count?: number;
  active: boolean;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={`inline-flex max-w-[200px] items-center gap-1.5 rounded-full border px-3 py-1 text-[12px] font-medium transition-colors ${
        active
          ? "border-[var(--primary)] bg-[var(--primary)] text-[var(--primary-foreground)]"
          : "border-[var(--border)] bg-[var(--card)] text-[var(--muted-foreground)] hover:border-[var(--primary)]/50 hover:text-[var(--foreground)]"
      }`}
    >
      <span className="truncate">{label}</span>
      {typeof count === "number" ? (
        <span
          className={`rounded-full px-1.5 text-[10px] font-semibold ${
            active
              ? "bg-[var(--primary-foreground)]/20"
              : "bg-[var(--muted)] text-[var(--muted-foreground)]"
          }`}
        >
          {count}
        </span>
      ) : null}
    </button>
  );
}
