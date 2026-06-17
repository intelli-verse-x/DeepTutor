"use client";

import { useCallback, useEffect, useState } from "react";
import { CheckCircle2, Loader2, XCircle } from "lucide-react";
import { useTranslation } from "react-i18next";

import {
  SettingRow,
  SettingSection,
  SettingsPageHeader,
} from "@/components/settings/shared";
import { MinerUEngineSettings } from "@/components/settings/MinerUEngineSettings";
import { Toggle } from "@/components/settings/Toggle";
import { apiFetch, apiUrl } from "@/lib/api";

type EngineMeta = {
  id: string;
  name: string;
  description: string;
  needs_local_models: boolean;
  available: boolean;
};

type Readiness = { ready: boolean; reason: string; message: string };

type DocumentParsingPayload = {
  engine: string;
  engines: Record<string, Record<string, unknown>>;
  available_engines: EngineMeta[];
  readiness: Record<string, Readiness>;
  mineru: { api_token_set: boolean; local_cli?: unknown };
};

const INSTALL_HINT: Record<string, string> = {
  docling: "pip install deeptutor[parse-docling]",
  markitdown: "pip install deeptutor[parse-markitdown]",
};

export default function DocumentParsingSettingsPage() {
  const { t } = useTranslation();
  const [data, setData] = useState<DocumentParsingPayload | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  const load = useCallback(async () => {
    setError(null);
    try {
      const response = await apiFetch(
        apiUrl("/api/v1/settings/document-parsing"),
      );
      const payload = (await response.json().catch(() => ({}))) as
        | DocumentParsingPayload
        | { detail?: string };
      if (!response.ok) {
        throw new Error(
          "detail" in payload && payload.detail
            ? payload.detail
            : t("Failed to load document parsing settings."),
        );
      }
      setData(payload as DocumentParsingPayload);
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setLoading(false);
    }
  }, [t]);

  useEffect(() => {
    void load();
  }, [load]);

  const putDocumentParsing = useCallback(
    async (body: Record<string, unknown>) => {
      setBusy(true);
      setError(null);
      try {
        const response = await apiFetch(
          apiUrl("/api/v1/settings/document-parsing"),
          {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body),
          },
        );
        const payload = (await response.json().catch(() => ({}))) as
          | DocumentParsingPayload
          | { detail?: string };
        if (!response.ok) {
          throw new Error(
            "detail" in payload && payload.detail
              ? payload.detail
              : t("Failed to save document parsing settings."),
          );
        }
        setData(payload as DocumentParsingPayload);
      } catch (err) {
        setError(err instanceof Error ? err.message : String(err));
      } finally {
        setBusy(false);
      }
    },
    [t],
  );

  return (
    <div>
      <SettingsPageHeader
        title={t("Document Parsing")}
        description={t(
          "How uploaded documents are converted into text for knowledge bases and question generation. Pick an engine and its options. Local model downloads are off by default — they only happen when you explicitly allow them.",
        )}
      />

      {loading && (
        <div className="flex items-center gap-2 text-[13px] text-[var(--muted-foreground)]">
          <Loader2 className="h-4 w-4 animate-spin" />
          {t("Loading...")}
        </div>
      )}

      {!loading && error && (
        <div className="mb-5 rounded-xl border border-red-500/30 bg-red-500/10 px-4 py-3 text-[13px] text-red-600 dark:text-red-300">
          {error}
        </div>
      )}

      {!loading && data && (
        <>
          <section className="mb-10">
            <header className="mb-3">
              <h2 className="text-[15px] font-semibold tracking-tight text-[var(--foreground)]">
                {t("Engine")}
              </h2>
              <p className="mt-1 text-[12.5px] leading-relaxed text-[var(--muted-foreground)]">
                {t(
                  "The active engine handles all parsing. Text-only is built in and extracts plain text; markitdown is lightweight and optional; MinerU and Docling produce richer structure but may need local models or a hosted API.",
                )}
              </p>
            </header>
            <div className="flex flex-col gap-2">
              {data.available_engines.map((engine) => {
                const active = engine.id === data.engine;
                return (
                  <button
                    key={engine.id}
                    type="button"
                    disabled={busy}
                    onClick={() =>
                      !active && putDocumentParsing({ engine: engine.id })
                    }
                    className={`flex items-start justify-between gap-4 rounded-xl border px-4 py-3 text-left transition-colors disabled:opacity-60 ${
                      active
                        ? "border-[var(--foreground)] bg-[var(--card)]"
                        : "border-[var(--border)] hover:border-[var(--foreground)]/40"
                    }`}
                  >
                    <div className="min-w-0">
                      <div className="flex items-center gap-2">
                        <span className="text-[13px] font-medium text-[var(--foreground)]">
                          {engine.name}
                        </span>
                        {active && (
                          <span className="rounded-full bg-[var(--foreground)] px-2 py-0.5 text-[10px] font-medium text-[var(--background)]">
                            {t("Active")}
                          </span>
                        )}
                        {!engine.available && (
                          <span className="rounded-full border border-[var(--border)] px-2 py-0.5 text-[10px] text-[var(--muted-foreground)]">
                            {t("Not installed")}
                          </span>
                        )}
                      </div>
                      <p className="mt-1 text-[12px] text-[var(--muted-foreground)]">
                        {engine.description}
                      </p>
                      {!engine.available && INSTALL_HINT[engine.id] && (
                        <code className="mt-1 block font-mono text-[11px] text-[var(--muted-foreground)]">
                          {INSTALL_HINT[engine.id]}
                        </code>
                      )}
                    </div>
                  </button>
                );
              })}
            </div>
          </section>

          {data.engine === "text_only" && <TextOnlyPanel />}

          {data.engine === "mineru" && <MinerUEngineSettings />}

          {data.engine === "docling" && (
            <DoclingPanel
              slice={data.engines.docling || {}}
              readiness={data.readiness.docling}
              available={
                data.available_engines.find((e) => e.id === "docling")
                  ?.available ?? false
              }
              busy={busy}
              onSave={(patch) =>
                putDocumentParsing({ engines: { docling: patch } })
              }
            />
          )}

          {data.engine === "markitdown" && (
            <MarkItDownPanel
              slice={data.engines.markitdown || {}}
              available={
                data.available_engines.find((e) => e.id === "markitdown")
                  ?.available ?? false
              }
              busy={busy}
              onSave={(patch) =>
                putDocumentParsing({ engines: { markitdown: patch } })
              }
            />
          )}
        </>
      )}
    </div>
  );
}

function TextOnlyPanel() {
  const { t } = useTranslation();
  return (
    <SettingSection
      title={t("Text-only")}
      description={t(
        "Built-in plain text extraction for PDF, Office, and text files. No optional parser package, model download, OCR, or layout reconstruction.",
      )}
    >
      <SettingRow
        title={t("Model status")}
        control={
          <ReadinessBadge
            readiness={{ ready: true, reason: "ready", message: "" }}
          />
        }
      />
    </SettingSection>
  );
}

function ReadinessBadge({ readiness }: { readiness?: Readiness }) {
  const { t } = useTranslation();
  if (!readiness) return null;
  return (
    <span
      className={`inline-flex items-center gap-1 text-[12px] ${
        readiness.ready
          ? "text-emerald-600 dark:text-emerald-400"
          : "text-amber-600 dark:text-amber-400"
      }`}
    >
      {readiness.ready ? (
        <CheckCircle2 className="h-3.5 w-3.5 shrink-0" />
      ) : (
        <XCircle className="h-3.5 w-3.5 shrink-0" />
      )}
      {readiness.ready ? t("Ready to parse.") : readiness.message}
    </span>
  );
}

function DoclingPanel({
  slice,
  readiness,
  available,
  busy,
  onSave,
}: {
  slice: Record<string, unknown>;
  readiness?: Readiness;
  available: boolean;
  busy: boolean;
  onSave: (patch: Record<string, unknown>) => void;
}) {
  const { t } = useTranslation();
  const doOcr = Boolean(slice.do_ocr);
  const doTables = slice.do_table_structure !== false;
  const allowDownload = Boolean(slice.allow_local_model_download);

  if (!available) {
    return (
      <SettingSection title={t("Docling")} description="">
        <SettingRow
          title={t("Docling isn't installed.")}
          description="pip install deeptutor[parse-docling]"
          control={null}
        />
      </SettingSection>
    );
  }

  return (
    <SettingSection
      title={t("Docling")}
      description={t(
        "Structured conversion of PDF/Office/HTML/images. Downloads layout/table models on first run.",
      )}
    >
      <SettingRow
        title={t("Model status")}
        control={<ReadinessBadge readiness={readiness} />}
      />
      <SettingRow
        title={t("Allow automatic model download")}
        description={t(
          "Off by default. When off, parsing fails with guidance instead of silently downloading models. Or pre-fetch with `docling-tools models download`.",
        )}
        control={
          <Toggle
            checked={allowDownload}
            disabled={busy}
            onChange={(v) => onSave({ allow_local_model_download: v })}
          />
        }
      />
      <SettingRow
        title={t("Recognize tables")}
        control={
          <Toggle
            checked={doTables}
            disabled={busy}
            onChange={(v) => onSave({ do_table_structure: v })}
          />
        }
      />
      <SettingRow
        title={t("OCR scanned pages")}
        description={t("Slower; enable for image-only PDFs.")}
        control={
          <Toggle
            checked={doOcr}
            disabled={busy}
            onChange={(v) => onSave({ do_ocr: v })}
          />
        }
      />
    </SettingSection>
  );
}

function MarkItDownPanel({
  slice,
  available,
  busy,
  onSave,
}: {
  slice: Record<string, unknown>;
  available: boolean;
  busy: boolean;
  onSave: (patch: Record<string, unknown>) => void;
}) {
  const { t } = useTranslation();
  const llmImages = Boolean(slice.enable_llm_image_description);

  if (!available) {
    return (
      <SettingSection title={t("markitdown")} description="">
        <SettingRow
          title={t("markitdown isn't installed.")}
          description="pip install deeptutor[parse-markitdown]"
          control={null}
        />
      </SettingSection>
    );
  }

  return (
    <SettingSection
      title={t("markitdown")}
      description={t(
        "Lightweight Markdown conversion with broad format support. No model downloads.",
      )}
    >
      <SettingRow
        title={t("Describe images with the vision model")}
        description={t(
          "Reserved — uses DeepTutor's vision model to caption images during conversion.",
        )}
        control={
          <Toggle
            checked={llmImages}
            disabled={busy}
            onChange={(v) => onSave({ enable_llm_image_description: v })}
          />
        }
      />
    </SettingSection>
  );
}
