from unittest.mock import Mock

import pytest

from main import UserService
from schemas.user import User


def test_register_saves_user_data() -> None:
    repository = Mock()
    service = UserService(repository)

    service.register(User("Alice", "alice@example.com", 30))

    repository.save.assert_called_once_with(
        {"name": "Alice", "email": "alice@example.com", "age": 30}
    )


def test_find_by_email_returns_user_from_repository_data() -> None:
    repository = Mock()
    repository.find_by_email.return_value = {
        "name": "Alice",
        "email": "alice@example.com",
        "age": 30,
    }
    service = UserService(repository)

    user = service.find_by_email("alice@example.com")

    assert user == User("Alice", "alice@example.com", 30)


def test_find_by_email_returns_none_when_repository_has_no_data() -> None:
    repository = Mock()
    repository.find_by_email.return_value = None
    service = UserService(repository)

    assert service.find_by_email("missing@example.com") is None


def test_register_raises_duplicate_email_error() -> None:
    repository = Mock()
    repository.save.side_effect = ValueError("duplicate email")
    service = UserService(repository)

    with pytest.raises(ValueError, match="duplicate email"):
        service.register(User("Alice", "alice@example.com", 30))
