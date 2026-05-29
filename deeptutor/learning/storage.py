from __future__ import annotations

from pathlib import Path
import threading
import time
import uuid

from deeptutor.learning.models import LearningProgress
from deeptutor.services.path_service import get_path_service

# Module-level lock so CAS semantics hold across all store instances.
_cas_lock = threading.Lock()


def _atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + f".tmp.{uuid.uuid4().hex}")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


class LearningStore:
    def __init__(self, root: Path | None = None) -> None:
        self._root = root or (get_path_service().get_workspace_dir() / "learning")
        self._root.mkdir(parents=True, exist_ok=True)

    def _path(self, book_id: str) -> Path:
        if "/" in book_id or "\\" in book_id or ".." in book_id or ":" in book_id:
            raise ValueError(f"Invalid book_id: {book_id!r}")
        return self._root / f"{book_id}.json"

    def save(self, progress: LearningProgress) -> None:
        import json

        with _cas_lock:
            progress.updated_at = time.time()
            progress.version += 1
            data = progress.model_dump(mode="json")
            text = json.dumps(data, ensure_ascii=False, indent=2)
            _atomic_write_text(self._path(progress.book_id), text)

    def save_cas(self, progress: LearningProgress, expected_version: int) -> bool:
        """Compare-and-swap save. Returns True if version matched and save succeeded."""
        import json

        with _cas_lock:
            current = self.load(progress.book_id)
            if current is None or current.version != expected_version:
                return False
            progress.version = expected_version + 1
            progress.updated_at = time.time()
            data = progress.model_dump(mode="json")
            text = json.dumps(data, ensure_ascii=False, indent=2)
            _atomic_write_text(self._path(progress.book_id), text)
            return True

    def load(self, book_id: str) -> LearningProgress | None:
        import json

        path = self._path(book_id)
        if not path.exists():
            return None
        data = json.loads(path.read_text(encoding="utf-8"))
        return LearningProgress.model_validate(data)

    def delete(self, book_id: str) -> None:
        path = self._path(book_id)
        if path.exists():
            path.unlink()
        qpath = self._questions_path(book_id)
        if qpath.exists():
            qpath.unlink()

    def exists(self, book_id: str) -> bool:
        return self._path(book_id).exists()

    def _questions_path(self, book_id: str) -> Path:
        if "/" in book_id or "\\" in book_id or ".." in book_id or ":" in book_id:
            raise ValueError(f"Invalid book_id: {book_id!r}")
        return self._root / "questions" / f"{book_id}.json"

    def save_question_answers(self, book_id: str, answers: dict[str, str]) -> None:
        """Save generated question answers for server-side grading.

        Merges into existing data. Preserves metadata (kp_id, module_id, etc.)
        from previous save_question_meta() calls for questions not overwritten.
        """
        import json

        path = self._questions_path(book_id)
        existing = self._load_raw_questions(book_id)
        for qid, ans in answers.items():
            if isinstance(existing.get(qid), dict):
                existing[qid]["answer"] = ans
            else:
                existing[qid] = ans
        text = json.dumps(existing, ensure_ascii=False, indent=2)
        _atomic_write_text(path, text)

    def load_question_answers(self, book_id: str) -> dict[str, str]:
        """Load question answers. Returns {} if none saved.

        Backward compatible: if a value is a dict (from save_question_meta),
        extracts the \"answer\" key.
        """
        import json

        path = self._questions_path(book_id)
        if not path.exists():
            return {}
        raw = json.loads(path.read_text(encoding="utf-8"))
        result = {}
        for qid, val in raw.items():
            if isinstance(val, dict):
                result[qid] = val.get("answer", "")
            else:
                result[qid] = val
        return result

    def save_question_meta(self, book_id: str, meta: dict) -> None:
        """Save question metadata (answer, kp_id, module_id, question_type).

        Merges into existing data. Values should be dicts like:
        {"answer": str, "knowledge_point_id": str, "module_id": str, "question_type": str}
        """
        import json

        path = self._questions_path(book_id)
        existing = self._load_raw_questions(book_id)
        existing.update(meta)
        text = json.dumps(existing, ensure_ascii=False, indent=2)
        _atomic_write_text(path, text)

    def load_question_meta(self, book_id: str) -> dict[str, dict]:
        """Load question metadata. Backward compatible with old str-value format.

        Returns: {question_id: {"answer": ..., "knowledge_point_id": ..., ...}}
        """
        raw = self._load_raw_questions(book_id)
        result = {}
        for qid, val in raw.items():
            if isinstance(val, str):
                result[qid] = {"answer": val, "knowledge_point_id": "", "module_id": "", "question_type": "short"}
            elif isinstance(val, dict):
                result[qid] = val
        return result

    def _load_raw_questions(self, book_id: str) -> dict:
        """Load raw questions JSON file. Returns {} if none saved."""
        import json

        path = self._questions_path(book_id)
        if not path.exists():
            return {}
        return json.loads(path.read_text(encoding="utf-8"))

    def list_all(self) -> list[str]:
        """Return all book_ids that have stored progress."""
        return sorted(
            p.stem
            for p in self._root.glob("*.json")
            if not p.name.startswith(".")
        )


__all__ = ["LearningStore"]
