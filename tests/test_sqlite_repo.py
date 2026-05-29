import pytest

from repos.sqlite_repo import SQLiteRepository


def test_sqlite_repository_saves_and_finds_data(tmp_path) -> None:
    repository = SQLiteRepository(str(tmp_path / "users.db"))
    data = {"name": "Alice", "email": "alice@example.com", "age": 30}

    repository.save(data)

    assert repository.find_by_email("alice@example.com") == data


def test_sqlite_repository_returns_none_for_missing_email(tmp_path) -> None:
    repository = SQLiteRepository(str(tmp_path / "users.db"))

    assert repository.find_by_email("missing@example.com") is None


def test_sqlite_repository_raises_duplicate_email_error(tmp_path) -> None:
    repository = SQLiteRepository(str(tmp_path / "users.db"))
    data = {"name": "Alice", "email": "alice@example.com", "age": 30}

    repository.save(data)

    with pytest.raises(ValueError, match="duplicate email"):
        repository.save(data)
