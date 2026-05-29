from repos.repository import Data


class InMemoryRepository:
    def __init__(self) -> None:
        self.all_data: dict[str, Data] = {}

    def save(self, data: Data) -> None:
        if data["email"] in self.all_data:
            raise ValueError("duplicate email")
        self.all_data[data["email"]] = data

    def find_by_email(self, email: str) -> Data | None:
        return self.all_data.get(email)
