import json

from repos.repository import Data


class JsonRepository:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.all_data = self._get_all_data()

    def _get_all_data(self) -> dict[str, Data]:
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save(self, data: Data) -> None:
        if data["email"] in self.all_data:
            raise ValueError("duplicate email")
        self.all_data[data["email"]] = data
        with open(self.file_path, "w") as f:
            json.dump(self.all_data, f)

    def find_by_email(self, email: str) -> Data | None:
        return self.all_data.get(email)
