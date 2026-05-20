"use client";

type JsonObject = Record<string, unknown>;

function isJsonObject(value: unknown): value is JsonObject {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function tryParseJson(text: string): unknown | null {
  try {
    return JSON.parse(text);
  } catch {
    return null;
  }
}

function splitStructuredContent(content: string): Array<string | unknown> {
  const trimmed = content.trim();
  if (!trimmed) return [];
  const whole = tryParseJson(trimmed);
  if (whole !== null) return [whole];
  const parts: Array<string | unknown> = [];
  for (const line of trimmed.split(/\n+/)) {
    const parsed = tryParseJson(line.trim());
    parts.push(parsed === null ? line : parsed);
  }
  return parts;
}

function renderValue(value: unknown): string {
  if (typeof value === "string" || typeof value === "number" || typeof value === "boolean") {
    return String(value);
  }
  if (Array.isArray(value)) {
    return value.map(renderValue).join(", ");
  }
  if (isJsonObject(value)) {
    return Object.entries(value)
      .map(([key, val]) => `${key}: ${renderValue(val)}`)
      .join("\n");
  }
  return "";
}

function renderQuestionPayload(question: unknown) {
  if (!isJsonObject(question)) {
    return <p className="text-sm text-[var(--foreground)] whitespace-pre-wrap">{renderValue(question)}</p>;
  }
  const options = Array.isArray(question.options) ? question.options : [];
  const entries = Object.entries(question).filter(([key]) => !["answer", "correct_answer", "solution", "options"].includes(key));
  return (
    <div className="space-y-3">
      {entries.map(([key, value]) => (
        <div key={key}>
          <div className="text-xs uppercase text-[var(--muted-foreground)]">{key}</div>
          <div className="text-sm text-[var(--foreground)] whitespace-pre-wrap">{renderValue(value)}</div>
        </div>
      ))}
      {options.length > 0 && (
        <div className="grid gap-2">
          {options.map((option, idx) => (
            <div key={idx} className="rounded border border-[var(--border)] px-3 py-2 text-sm">
              {renderValue(option)}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function renderQuestionCard(question: unknown, questionId?: unknown) {
  return (
    <div className="rounded-lg border border-[var(--border)] bg-[var(--background)] p-4 shadow-sm">
      {questionId ? (
        <div className="mb-3 font-mono text-xs text-[var(--muted-foreground)]">{String(questionId)}</div>
      ) : null}
      {renderQuestionPayload(question)}
    </div>
  );
}

export function latestQuestionIdFromContent(content: string): string {
  const parts = splitStructuredContent(content);
  for (let i = parts.length - 1; i >= 0; i -= 1) {
    const part = parts[i];
    if (isJsonObject(part) && typeof part.question_id === "string") {
      return part.question_id;
    }
    if (isJsonObject(part) && Array.isArray(part.question_ids) && part.question_ids.length > 0) {
      const last = part.question_ids[part.question_ids.length - 1];
      return typeof last === "string" ? last : "";
    }
  }
  return "";
}

function renderStructuredItem(item: unknown, index: number) {
  if (typeof item === "string") {
    return <p key={index} className="whitespace-pre-wrap">{item}</p>;
  }
  if (isJsonObject(item) && "question" in item) {
    return <div key={index}>{renderQuestionCard(item.question, item.question_id)}</div>;
  }
  if (isJsonObject(item)) {
    const questions = Array.isArray(item.questions) ? item.questions : Array.isArray(item.exercises) ? item.exercises : [];
    const questionIds = Array.isArray(item.question_ids) ? item.question_ids : [];
    if (questions.length > 0) {
      return (
        <div key={index} className="space-y-3">
          {questions.map((question, qIndex) => (
            <div key={qIndex}>{renderQuestionCard(question, questionIds[qIndex])}</div>
          ))}
        </div>
      );
    }
  }
  return <pre key={index} className="whitespace-pre-wrap text-sm">{renderValue(item)}</pre>;
}

export function StructuredStageContent({ content }: { content: string }) {
  const parts = splitStructuredContent(content);
  return <div className="space-y-4">{parts.map(renderStructuredItem)}</div>;
}
