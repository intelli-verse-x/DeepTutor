from __future__ import annotations


def test_book_session_and_tutorbot_ids_are_scoped_per_user(as_user) -> None:
    from deeptutor.book.storage import BookStorage
    from deeptutor.services.session import get_sqlite_session_store, get_turn_runtime_manager
    from deeptutor.services.tutorbot.manager import TutorBotManager

    tutorbot_manager = TutorBotManager()
    shared_book_id = "shared-book-id"

    with as_user("u_victim"):
        victim_book_root = BookStorage().book_root(shared_book_id)
        victim_session_db = get_sqlite_session_store().db_path
        victim_runtime_store_db = get_turn_runtime_manager().store.db_path
        victim_tutorbot_dir = tutorbot_manager._tutorbot_dir

    with as_user("u_attacker"):
        attacker_book_root = BookStorage().book_root(shared_book_id)
        attacker_session_db = get_sqlite_session_store().db_path
        attacker_runtime_store_db = get_turn_runtime_manager().store.db_path
        attacker_tutorbot_dir = tutorbot_manager._tutorbot_dir

    assert victim_book_root != attacker_book_root
    assert victim_session_db != attacker_session_db
    assert victim_runtime_store_db != attacker_runtime_store_db
    assert victim_tutorbot_dir != attacker_tutorbot_dir
    assert "u_victim" in str(victim_book_root)
    assert "u_attacker" in str(attacker_book_root)
