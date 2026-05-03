"""Knowledge-Base write helpers (KB v2).

Producers
---------
* :func:`push_user_chat`               — chat turn  -> qv_u_<uid>_chat
* :func:`push_user_diagnostic`         — diagnostic answer -> qv_u_<uid>_diagnostic
* :func:`push_user_score_prediction`   — score prediction  -> qv_u_<uid>_insights
* :func:`push_exam_paper_questions`    — generated paper   -> qv_exam_<slug>_questions
*

This package centralises *outbound* writes from DeepTutor into the
QuizVerse Memory Service via the BFF webhook at
``POST /api/kb/ingest/<source>``. Read-side calls still go through
``deeptutor.services.rag``.

All write helpers are designed to be **fire-and-forget**: they swallow
their own errors and never block the calling request. Schedule them
via ``asyncio.create_task(...)`` after the relevant DB commit.
"""

from deeptutor.services.kb.exam_kb_writer import (
    normalize_exam_slug,
    push_exam_paper_questions,
)
from deeptutor.services.kb.user_kb_writer import (
    push_user_chat,
    push_user_diagnostic,
    push_user_score_prediction,
)

__all__ = [
    "push_user_chat",
    "push_user_diagnostic",
    "push_user_score_prediction",
    "push_exam_paper_questions",
    "normalize_exam_slug",
]
