"""Import all model modules so Base.metadata knows about every table."""

from deeptutor.services.db.models.memory import UserMemory  # noqa: F401
from deeptutor.services.db.models.session import (  # noqa: F401
    ChatSession,
    ChatMessage,
    ChatTurn,
    ChatTurnEvent,
)
from deeptutor.services.db.models.notebook import Notebook, NotebookRecord  # noqa: F401
from deeptutor.services.db.models.knowledge_base import (  # noqa: F401
    KnowledgeBaseModel,
    KBDocument,
    KBChunk,
)
from deeptutor.services.db.models.guide import GuideSessionModel  # noqa: F401
