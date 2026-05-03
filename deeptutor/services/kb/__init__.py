"""Knowledge-Base write helpers (KB v2).

This package centralises *outbound* writes from DeepTutor into the
QuizVerse Memory Service via the BFF webhook at
``POST /api/kb/ingest/<source>``. Read-side calls still go through
``deeptutor.services.rag``.

Currently shipped:

* :func:`deeptutor.services.kb.user_kb_writer.push_user_chat` — fires
  one document per (user, session, turn) into ``qv_u_<uid>_chat``.

All write helpers are designed to be **fire-and-forget**: they swallow
their own errors and never block the calling request.
"""

from deeptutor.services.kb.user_kb_writer import push_user_chat

__all__ = ["push_user_chat"]
