"use client";

import { useParams } from "next/navigation";
import { useEffect, useState, useRef, useCallback } from "react";
import { Lightbulb, Loader2 } from "lucide-react";
import { useTranslation } from "react-i18next";
import { wsUrl } from "@/lib/api";

interface StreamEvent {
  type: string;
  source: string;
  stage: string;
  content: string;
  metadata: Record<string, unknown>;
}

interface StageProgress {
  stage: string;
  status: "pending" | "active" | "completed" | "error";
  content: string;
}

const STAGE_LABELS: Record<string, string> = {
  diagnostic_phase1: "Diagnostic Phase 1",
  diagnostic_phase2: "Diagnostic Phase 2",
  metacognitive_intro: "Metacognitive Intro",
  plan: "Study Plan",
  pretest: "Pretest",
  explain: "Explain",
  feynman_check: "Feynman Check",
  practice: "Practice",
  error_diagnosis: "Error Diagnosis",
  module_test: "Module Test",
  review: "Review",
  completed: "Completed",
};

export default function LearningBookPage() {
  const params = useParams<{ bookId: string }>();
  const { t } = useTranslation();
  const [stages, setStages] = useState<StageProgress[]>([]);
  const [currentStage, setCurrentStage] = useState<string>("");
  const currentStageRef = useRef<string>("");
  const [connecting, setConnecting] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const wsRef = useRef<WebSocket | null>(null);

  const connect = useCallback(() => {
    const ws = new WebSocket(wsUrl("/api/v1/ws"));
    wsRef.current = ws;

    ws.onopen = () => {
      setConnecting(false);
      setError(null);
      ws.send(JSON.stringify({
        type: "start_turn",
        session_id: params.bookId,
        capability: "guided_learning",
        content: "Start learning",
        book_references: [{ book_id: params.bookId, page_ids: [] }],
        config: {},
      }));
    };

    ws.onmessage = (event) => {
      try {
        const evt: StreamEvent = JSON.parse(event.data);
        handleStreamEvent(evt);
      } catch { /* ignore parse errors */ }
    };

    ws.onerror = () => setError("Connection error");
    ws.onclose = () => setConnecting(true);
  }, [params.bookId]);

  const handleStreamEvent = (evt: StreamEvent) => {
    if (evt.type === "stage_start") {
      currentStageRef.current = evt.stage;
      setCurrentStage(evt.stage);
      setStages(prev => {
        const updated = [...prev];
        const idx = updated.findIndex(s => s.stage === evt.stage);
        if (idx >= 0) {
          updated[idx] = { ...updated[idx], status: "active" };
        } else {
          updated.push({ stage: evt.stage, status: "active", content: "" });
        }
        return updated;
      });
    } else if (evt.type === "content") {
      setStages(prev => prev.map(s =>
        s.stage === currentStageRef.current ? { ...s, content: s.content + evt.content } : s
      ));
    } else if (evt.type === "result" || evt.type === "stage_end") {
      setStages(prev => prev.map(s =>
        s.stage === currentStageRef.current ? { ...s, status: "completed" } : s
      ));
      currentStageRef.current = "";
      setCurrentStage("");
    } else if (evt.type === "error") {
      setError(evt.content);
      setStages(prev => prev.map(s =>
        s.stage === currentStageRef.current ? { ...s, status: "error" } : s
      ));
    }
  };

  useEffect(() => {
    connect();
    return () => { wsRef.current?.close(); };
  }, [connect]);

  return (
    <div className="flex h-full">
      {/* Stage sidebar */}
      <div className="w-64 border-r border-[var(--border)] p-4 overflow-y-auto">
        <h2 className="text-sm font-semibold mb-3 flex items-center gap-2">
          <Lightbulb className="w-4 h-4 text-[var(--primary)]" />
          Learning Stages
        </h2>
        {connecting && <Loader2 className="w-4 h-4 animate-spin text-[var(--muted-foreground)]" />}
        {stages.map((s) => (
          <div key={s.stage} className="flex items-center gap-2 py-1 text-sm">
            <span className={s.status === "completed" ? "text-green-500" : s.status === "error" ? "text-red-500" : "text-[var(--muted-foreground)]"}>
              {s.status === "active" ? <Loader2 className="w-3 h-3 animate-spin" /> :
               s.status === "completed" ? "✓" : s.status === "error" ? "✗" : "○"}
            </span>
            <span className={s.status === "active" ? "text-[var(--foreground)]" : "text-[var(--muted-foreground)]"}>
              {STAGE_LABELS[s.stage] || s.stage}
            </span>
          </div>
        ))}
      </div>
      {/* Content area */}
      <div className="flex-1 p-8 overflow-y-auto">
        {error && <div className="text-red-500 mb-4">{error}</div>}
        {(stages.find(s => s.status === "active") || stages.find(s => s.status === "completed" && s.content))?.content ? (
          <div className="prose dark:prose-invert max-w-none whitespace-pre-wrap">
            {(stages.find(s => s.status === "active") || stages.find(s => s.status === "completed" && s.content))?.content}
          </div>
        ) : (
          <div className="flex items-center justify-center h-full text-[var(--muted-foreground)]">
            {connecting ? <Loader2 className="w-8 h-8 animate-spin" /> : "Ready to start learning"}
          </div>
        )}
      </div>
    </div>
  );
}
