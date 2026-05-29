from repos.sqlite_repo import SQLiteRepository
from repos.repository import Repository
from schemas.user import User


class UserService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def register(self, user: User) -> None:
        self.repository.save(user.__dict__)

    def find_by_email(self, email: str) -> User | None:
        data = self.repository.find_by_email(email)
        if data is None:
            return None
        return User(**data)


if __name__ == "__main__":
    sqlite_repo = SQLiteRepository("users.db")
    user_service = UserService(sqlite_repo)
    user1 = User("Alice", "alice@example.com", 30)
    user_service.register(user1)
    print(user_service.find_by_email("alice@example.com"))
