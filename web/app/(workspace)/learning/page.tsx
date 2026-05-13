"use client";

import { useEffect, useState, useCallback } from "react";
import { useRouter } from "next/navigation";
import { BookOpen, Loader2, Play } from "lucide-react";
import { useTranslation } from "react-i18next";
import { fetchProgress } from "@/lib/learning-api";

interface ModuleSummary {
  id: string;
  name: string;
  order: number;
  pass_threshold: number;
  knowledge_points: { id: string; name: string }[];
}

export default function LearningPage() {
  const router = useRouter();
  const { t } = useTranslation();
  const [modules, setModules] = useState<ModuleSummary[]>([]);
  const [masteryLevels, setMasteryLevels] = useState<Record<string, number>>({});
  const [loading, setLoading] = useState(true);
  const [toast, setToast] = useState("");

  useEffect(() => {
    if (!toast) return;
    const timer = setTimeout(() => setToast(""), 3500);
    return () => clearTimeout(timer);
  }, [toast]);

  const loadProgress = useCallback(async () => {
    try {
      const data = await fetchProgress("default");
      setModules(data.modules ?? []);
      setMasteryLevels(data.mastery_levels ?? {});
    } catch {
      setToast(t("guidedLearning.connectionError"));
    } finally {
      setLoading(false);
    }
  }, [t]);

  useEffect(() => {
    loadProgress();
  }, [loadProgress]);

  const masteredCount = (mod: ModuleSummary) =>
    mod.knowledge_points.filter(
      (kp) => (masteryLevels[kp.id] ?? 0) >= mod.pass_threshold,
    ).length;

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
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-2xl font-bold">{t("guidedLearning.title")}</h1>
          <p className="text-[var(--muted-foreground)] text-sm mt-1">
            {modules.length > 0
              ? `${modules.length} ${t("guidedLearning.modules")}`
              : t("guidedLearning.description")}
          </p>
        </div>
        <button
          onClick={() => router.push("/learning/default")}
          className="flex items-center gap-2 px-4 py-2 rounded-lg bg-[var(--primary)] text-[var(--primary-foreground)] text-sm font-medium hover:opacity-90 transition-opacity"
        >
          <Play className="w-4 h-4" />
          {t("guidedLearning.startLearning")}
        </button>
      </div>

      {modules.length === 0 ? (
        <div className="flex flex-col items-center justify-center py-20 text-[var(--muted-foreground)]">
          <BookOpen className="w-12 h-12 mb-4 opacity-50" />
          <p className="text-lg font-medium">{t("guidedLearning.noModules")}</p>
          <p className="text-sm mt-1">
            {t("guidedLearning.description")}
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {modules
            .sort((a, b) => a.order - b.order)
            .map((mod) => {
              const mastered = masteredCount(mod);
              const total = mod.knowledge_points.length;
              const pct = total > 0 ? Math.round((mastered / total) * 100) : 0;

              return (
                <div
                  key={mod.id}
                  className="p-5 rounded-xl border border-[var(--border)] bg-[var(--card)]"
                >
                  <h3 className="font-semibold text-[var(--foreground)] truncate">
                    {mod.name}
                  </h3>
                  <p className="text-sm text-[var(--muted-foreground)] mt-1">
                    {t("guidedLearning.moduleProgress", { count: total })}
                  </p>
                  {total > 0 && (
                    <div className="mt-3">
                      <div className="flex items-center justify-between text-xs text-[var(--muted-foreground)] mb-1">
                        <span>{t("guidedLearning.masteredProgress", { mastered, total })}</span>
                        <span>{pct}%</span>
                      </div>
                      <div className="w-full h-1.5 rounded-full bg-[var(--muted)]">
                        <div
                          className="h-full rounded-full bg-[var(--primary)] transition-all"
                          style={{ width: `${pct}%` }}
                        />
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
        </div>
      )}
    </div>
  );
}
