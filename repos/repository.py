from typing import Any, Protocol

Data = dict[str, Any]


class Repository(Protocol):
    def save(self, data: Data) -> None: ...

    def find_by_email(self, email: str) -> Data | None: ...
