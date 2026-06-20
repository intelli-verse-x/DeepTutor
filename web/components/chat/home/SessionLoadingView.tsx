"use client";

import { useEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import { Loader2, X } from "lucide-react";

/**
 * Loading overlay shown while a chat session is being fetched from the
 * server.  Progress is cosmetic but asymptotically approaches 99 % so
 * the user sees continuous activity.  Completion jumps to 100 % and fades.
 */
interface SessionLoadingViewProps {
  stage: "loading" | "complete";
  onCancel?: () => void;
}

// ---- timing constants ----
const FAST_MS = 600; // 0 → 45 %  (quick)
const SLOW_MS = 4000; // 45 → 90 % (eased)
const TAIL_MS = 20_000; // 90 → 99 % (asymptotic)
const FAST_PEAK = 45;
const SLOW_PEAK = 90;
const TAIL_ASYM = 99;

const STILL_LOADING_AFTER_MS = 8000;

export default function SessionLoadingView({
  stage,
  onCancel,
}: SessionLoadingViewProps) {
  const { t } = useTranslation();
  const [progress, setProgress] = useState(0);
  const [showHint, setShowHint] = useState(false);
  const startRef = useRef<number>(0);
  const rafRef = useRef<number>(0);
  const hintTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    if (stage === "complete") {
      setProgress(100);
      setShowHint(false);
      if (hintTimerRef.current) clearTimeout(hintTimerRef.current);
      return;
    }

    // Reset
    startRef.current = Date.now();
    setProgress(0);
    setShowHint(false);
    if (hintTimerRef.current) clearTimeout(hintTimerRef.current);
    hintTimerRef.current = setTimeout(
      () => setShowHint(true),
      STILL_LOADING_AFTER_MS,
    );

    const tick = () => {
      const elapsed = Date.now() - startRef.current;
      let value: number;

      if (elapsed <= FAST_MS) {
        value = (elapsed / FAST_MS) * FAST_PEAK;
      } else if (elapsed <= FAST_MS + SLOW_MS) {
        const t2 = (elapsed - FAST_MS) / SLOW_MS; // 0…1
        value =
          FAST_PEAK + (SLOW_PEAK - FAST_PEAK) * (1 - Math.pow(1 - t2, 2));
      } else {
        const t3 = (elapsed - FAST_MS - SLOW_MS) / TAIL_MS; // 0 → 1
        value = SLOW_PEAK + (TAIL_ASYM - SLOW_PEAK) * (1 - 1 / (1 + 3 * t3));
      }

      setProgress(Math.min(Math.round(value), 99));
      rafRef.current = requestAnimationFrame(tick);
    };
    rafRef.current = requestAnimationFrame(tick);

    return () => {
      cancelAnimationFrame(rafRef.current);
      if (hintTimerRef.current) clearTimeout(hintTimerRef.current);
    };
  }, [stage]);

  return (
    <div className="relative flex h-full flex-col items-center justify-center gap-5 px-6">
      {/* Cancel button — top-right */}
      {onCancel ? (
        <button
          type="button"
          aria-label={t("Cancel")}
          onClick={onCancel}
          className="absolute end-3 top-3 inline-flex h-8 w-8 items-center justify-center rounded-lg text-[var(--muted-foreground)] transition hover:bg-[var(--muted)] hover:text-[var(--foreground)])"
        >
          <X className="h-4 w-4" />
        </button>
      ) : null}

      {/* Logo */}
      <div className="flex items-center gap-3">
        <img
          src="/logo_black.png"
          alt="DeepTutor"
          width={32}
          height={32}
          className="h-8 w-8 select-none"
          draggable={false}
        />
        <Loader2 className="h-5 w-5 animate-spin text-[var(--primary)]" />
      </div>

      {/* Primary message */}
      <p className="text-sm font-medium text-[var(--foreground)]">
        {t("Loading conversation")}
      </p>

      {/* Progress bar */}
      <div className="flex w-56 items-center gap-3">
        <div className="h-1.5 flex-1 overflow-hidden rounded-full bg-[var(--muted)]">
          <div
            className="h-full rounded-full bg-[var(--primary)] transition-[width] duration-300 ease-out"
            style={{ width: `${progress}%` }}
          />
        </div>
        <span className="w-8 text-right text-[11px] tabular-nums text-[var(--muted-foreground)]">
          {progress}%
        </span>
      </div>

      {/* Slow-load hint */}
      {showHint ? (
        <p className="animate-fade-in text-[12px] text-[var(--muted-foreground)]">
          {t("Still loading…")}
        </p>
      ) : null}
    </div>
  );
}
