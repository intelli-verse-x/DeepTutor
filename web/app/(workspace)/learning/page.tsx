"use client";

import { useEffect, useState, useCallback } from "react";
import { useRouter } from "next/navigation";
import {
  BookOpen,
  Loader2,
  Play,
  Plus,
  RotateCcw,
  Trash2,
} from "lucide-react";
import { useTranslation } from "react-i18next";
import {
  fetchAllProgress,
  deleteProgress,
  redoProgress,
  type ProgressSummary,
} from "@/lib/learning-api";
import CreateModuleDialog from "@/components/learning/CreateModuleDialog";

type Tab = "current" | "completed" | "all";

export default function LearningPage() {
  const router = useRouter();
  const { t } = useTranslation();
  const [items, setItems] = useState<ProgressSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [tab, setTab] = useState<Tab>("all");
  const [toast, setToast] = useState("");
  const [dialogOpen, setDialogOpen] = useState(false);

  const loadProgress = useCallback(async () => {
    try {
      const result = await fetchAllProgress();
      setItems(result.summaries ?? []);
      if (result.errors?.length) {
        console.warn("Some progress failed to load:", result.errors);
      }
    } catch {
      setToast(t("guidedLearning.connectionError"));
    } finally {
      setLoading(false);
    }
  }, [t]);

  useEffect(() => {
    loadProgress();
  }, [loadProgress]);

  useEffect(() => {
    if (!toast) return;
    const timer = setTimeout(() => setToast(""), 3500);
    return () => clearTimeout(timer);
  }, [toast]);

  const filtered = items.filter((it) => {
    if (tab === "current") return it.current_stage !== "completed";
    if (tab === "completed") return it.current_stage === "completed";
    return true;
  });

  const tabs: { key: Tab; label: string }[] = [
    { key: "current", label: t("guidedLearning.tabCurrent") },
    { key: "completed", label: t("guidedLearning.tabCompleted") },
    { key: "all", label: t("guidedLearning.tabAll") },
  ];

  if (loading) {
    return (
      <div className="flex items-center justify-center h-full">
        <Loader2 className="w-8 h-8 animate-spin text-[var(--muted-foreground)]" />
      </div>
    );
  }

  return (
    <div className="p-8 max-w-4xl mx-auto">
      {toast && (
        <div className="fixed top-4 right-4 z-50 rounded-lg bg-red-500/90 px-4 py-2 text-sm text-white shadow-lg">
          {toast}
        </div>
      )}

      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-2xl font-bold">{t("guidedLearning.title")}</h1>
          <p className="text-[var(--muted-foreground)] text-sm mt-1">
            {t("guidedLearning.description")}
          </p>
        </div>
        <button
          onClick={() => setDialogOpen(true)}
          className="flex items-center gap-2 px-4 py-2 rounded-lg bg-[var(--primary)] text-[var(--primary-foreground)] text-sm font-medium hover:opacity-90 transition-opacity"
        >
          <Plus className="w-4 h-4" />
          {t("guidedLearning.createModule")}
        </button>
      </div>

      {/* Tabs */}
      <div className="flex gap-1 mb-6 border-b border-[var(--border)]">
        {tabs.map((tabItem) => (
          <button
            key={tabItem.key}
            onClick={() => setTab(tabItem.key)}
            className={`px-4 py-2 text-sm font-medium transition-colors border-b-2 -mb-px ${
              tab === tabItem.key
                ? "border-[var(--primary)] text-[var(--foreground)]"
                : "border-transparent text-[var(--muted-foreground)] hover:text-[var(--foreground)]"
            }`}
          >
            {tabItem.label}
          </button>
        ))}
      </div>

      {/* Content */}
      {filtered.length === 0 ? (
        <div className="flex flex-col items-center justify-center py-20 text-[var(--muted-foreground)]">
          <BookOpen className="w-12 h-12 mb-4 opacity-50" />
          <p className="text-lg font-medium">{t("guidedLearning.noModules")}</p>
          <p className="text-sm mt-1">{t("guidedLearning.description")}</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {filtered
            .sort((a, b) => (b.updated_at ?? 0) - (a.updated_at ?? 0))
            .map((card) => (
              <div
                key={card.book_id}
                className="p-5 rounded-xl border border-[var(--border)] bg-[var(--card)]"
              >
                <h3 className="font-semibold text-[var(--foreground)] truncate">
                  {card.name || card.book_id}
                </h3>
                <p className="text-sm text-[var(--muted-foreground)] mt-1">
                  {card.modules_count} {t("guidedLearning.modules")} ·{" "}
                  {card.kp_count} {t("guidedLearning.knowledgePoints")}
                </p>

                {/* Mastery bar */}
                {card.kp_count > 0 && (
                  <div className="mt-3">
                    <div className="flex items-center justify-between text-xs text-[var(--muted-foreground)] mb-1">
                      <span>{t("guidedLearning.mastered")}</span>
                      <span>{card.avg_mastery_pct}%</span>
                    </div>
                    <div className="w-full h-1.5 rounded-full bg-[var(--muted)]">
                      <div
                        className="h-full rounded-full bg-[var(--primary)] transition-all"
                        style={{ width: `${card.avg_mastery_pct}%` }}
                      />
                    </div>
                  </div>
                )}

                {/* Timestamp */}
                {card.updated_at > 0 && (
                  <p className="text-xs text-[var(--muted-foreground)] mt-2">
                    {new Date(card.updated_at * 1000).toLocaleDateString()}
                  </p>
                )}

                {/* Actions */}
                <div className="flex items-center gap-2 mt-3 pt-3 border-t border-[var(--border)]">
                  <button
                    onClick={() => router.push(`/learning/${card.book_id}`)}
                    className="flex items-center gap-1 px-3 py-1.5 text-xs rounded-lg bg-[var(--primary)] text-[var(--primary-foreground)] hover:opacity-90"
                  >
                    <Play className="w-3.5 h-3.5" />
                    {t("guidedLearning.continueLearning")}
                  </button>

                  <button
                    onClick={async () => {
                      if (!confirm(t("guidedLearning.redoConfirm"))) return;
                      try {
                        await redoProgress(card.book_id);
                        loadProgress();
                      } catch {
                        setToast(t("guidedLearning.redoFailed"));
                      }
                    }}
                    className="flex items-center gap-1 px-3 py-1.5 text-xs rounded-lg border border-[var(--border)] text-[var(--muted-foreground)] hover:text-[var(--foreground)] hover:bg-[var(--background)]/60"
                  >
                    <RotateCcw className="w-3.5 h-3.5" />
                    {t("guidedLearning.redo")}
                  </button>

                  <button
                    onClick={async () => {
                      if (!confirm(t("guidedLearning.deleteConfirm"))) return;
                      try {
                        await deleteProgress(card.book_id);
                        loadProgress();
                      } catch {
                        setToast(t("guidedLearning.deleteFailed"));
                      }
                    }}
                    className="flex items-center gap-1 px-3 py-1.5 text-xs rounded-lg text-red-500 hover:bg-red-500/10"
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                    {t("guidedLearning.delete")}
                  </button>
                </div>
              </div>
            ))}
        </div>
      )}

      <CreateModuleDialog
        open={dialogOpen}
        onClose={() => setDialogOpen(false)}
        onCreated={() => loadProgress()}
      />
    </div>
  );
}
