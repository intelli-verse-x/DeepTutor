"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import { useTranslation } from "react-i18next";
import { AlertTriangle, CheckCircle2, Loader2, Store, X } from "lucide-react";

import { installSkillFromHub } from "@/lib/skills-api";

// The live EduHub skill registry. Overridable for local dev (point both this
// and the backend `eduhub` hub at the same local server to test end-to-end).
const EDUHUB_BASE = (
  process.env.NEXT_PUBLIC_EDUHUB_URL || "https://eduhub.deeptutor.info"
).replace(/\/+$/, "");

interface InstallMessage {
  source: "eduhub";
  type: "install";
  slug: string;
  version?: string;
  name?: string;
}

function isInstallMessage(data: unknown): data is InstallMessage {
  if (typeof data !== "object" || data === null) return false;
  const d = data as Record<string, unknown>;
  return (
    d.source === "eduhub" &&
    d.type === "install" &&
    typeof d.slug === "string" &&
    d.slug.length > 0
  );
}

type Status =
  | { kind: "idle" }
  | { kind: "installing"; name: string }
  | { kind: "done"; name: string; version: string; verdict: string }
  | { kind: "error"; name: string; message: string };

export default function EduHubImportModal({
  onClose,
  onInstalled,
}: {
  onClose: () => void;
  onInstalled: () => void;
}) {
  const { i18n } = useTranslation();
  const zh = i18n.language?.toLowerCase().startsWith("zh");
  const tr = useCallback((cn: string, en: string) => (zh ? cn : en), [zh]);

  const [status, setStatus] = useState<Status>({ kind: "idle" });

  const origin = useMemo(() => {
    try {
      return new URL(EDUHUB_BASE).origin;
    } catch {
      return "";
    }
  }, []);

  const iframeSrc = `${EDUHUB_BASE}/skills?embed=deeptutor`;

  // Install requests arrive as postMessages from the embedded EduHub page.
  useEffect(() => {
    async function onMessage(event: MessageEvent) {
      if (origin && event.origin !== origin) return;
      if (!isInstallMessage(event.data)) return;
      const { slug, version, name } = event.data;
      const label = name || slug;
      // Build the ref ourselves (hardcoded `eduhub:` hub) so a spoofed message
      // can never redirect the install to a different registry.
      const ref = `eduhub:${slug}${version ? `@${version}` : ""}`;
      setStatus({ kind: "installing", name: label });
      try {
        const result = await installSkillFromHub(ref);
        setStatus({
          kind: "done",
          name: result.name || label,
          version: result.version,
          verdict: result.verdict.status,
        });
        onInstalled();
      } catch (err) {
        setStatus({
          kind: "error",
          name: label,
          message: err instanceof Error ? err.message : String(err),
        });
      }
    }
    window.addEventListener("message", onMessage);
    return () => window.removeEventListener("message", onMessage);
  }, [origin, onInstalled]);

  // Escape closes.
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if (e.key === "Escape") onClose();
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-[var(--overlay)] p-4"
      role="dialog"
      aria-modal="true"
      onClick={onClose}
    >
      <div
        className="flex h-[88vh] w-full max-w-5xl flex-col overflow-hidden rounded-xl border border-[var(--border)] bg-[var(--background)] shadow-2xl"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center justify-between border-b border-[var(--border)] px-5 py-3">
          <div className="flex items-center gap-2">
            <Store size={15} className="text-[var(--muted-foreground)]" />
            <h3 className="text-[14px] font-semibold text-[var(--foreground)]">
              {tr("从 EduHub 导入技能", "Import skills from EduHub")}
            </h3>
          </div>
          <button
            onClick={onClose}
            aria-label={tr("关闭", "Close")}
            className="rounded-md p-1 text-[var(--muted-foreground)] transition-colors hover:bg-[var(--muted)] hover:text-[var(--foreground)]"
          >
            <X size={16} />
          </button>
        </div>

        <StatusBanner status={status} tr={tr} />

        <iframe
          src={iframeSrc}
          title="EduHub"
          className="min-h-0 flex-1 border-0 bg-white"
        />
      </div>
    </div>
  );
}

function StatusBanner({
  status,
  tr,
}: {
  status: Status;
  tr: (cn: string, en: string) => string;
}) {
  if (status.kind === "idle") return null;

  if (status.kind === "installing") {
    return (
      <div className="flex items-center gap-2 border-b border-[var(--border)] bg-[var(--muted)]/40 px-5 py-2.5 text-[12.5px] text-[var(--foreground)]">
        <Loader2
          size={14}
          className="animate-spin text-[var(--muted-foreground)]"
        />
        {tr(`正在导入 ${status.name}…`, `Importing ${status.name}…`)}
      </div>
    );
  }

  if (status.kind === "done") {
    return (
      <div className="flex items-center gap-2 border-b border-emerald-500/20 bg-emerald-500/10 px-5 py-2.5 text-[12.5px] text-emerald-700 dark:text-emerald-400">
        <CheckCircle2 size={14} className="shrink-0" />
        <span>
          {tr(
            `已导入 ${status.name}${status.version ? `（${status.version}）` : ""}`,
            `Imported ${status.name}${status.version ? ` (${status.version})` : ""}`,
          )}
          {status.verdict === "unknown" &&
            tr(
              " · 此包未经验证，使用前请自行确认。",
              " · unverified package — review before use.",
            )}
        </span>
      </div>
    );
  }

  return (
    <div className="flex items-center gap-2 border-b border-amber-500/20 bg-amber-500/10 px-5 py-2.5 text-[12.5px] text-amber-700 dark:text-amber-400">
      <AlertTriangle size={14} className="shrink-0" />
      <span>
        {tr(`导入 ${status.name} 失败：`, `Could not import ${status.name}: `)}
        {status.message}
      </span>
    </div>
  );
}
