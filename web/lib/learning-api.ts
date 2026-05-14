import { apiUrl, apiFetch } from "./api";

export interface AnswerRequest {
  question_id: string;
  knowledge_point_id: string;
  module_id?: string;
  user_answer: string;
  expected_answer: string;
  self_attribution?: string;
}

export interface ModuleInit {
  id: string;
  name: string;
  order: number;
  pass_threshold?: number;
  knowledge_points: { id: string; name: string; type: string; module_id: string }[];
}

export async function fetchProgress(bookId: string) {
  const res = await apiFetch(apiUrl(`/api/v1/learning/progress/${bookId}`));
  if (!res.ok) throw new Error(`Failed to fetch progress: ${res.status}`);
  return res.json();
}

export async function submitAnswer(bookId: string, body: AnswerRequest) {
  const res = await apiFetch(apiUrl(`/api/v1/learning/progress/${bookId}/answer`), {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error(`Failed to submit answer: ${res.status}`);
  return res.json();
}

export async function initModules(bookId: string, modules: ModuleInit[]) {
  const res = await apiFetch(apiUrl(`/api/v1/learning/progress/${bookId}/init-modules`), {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ modules }),
  });
  if (!res.ok) throw new Error(`Failed to init modules: ${res.status}`);
  return res.json();
}
