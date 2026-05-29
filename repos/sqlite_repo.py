import sqlite3
from pathlib import Path

from repos.repository import Data


class SQLiteRepository:
    def __init__(self, database_path: str) -> None:
        self.database_path = database_path
        self._create_table()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.database_path)

    def _create_table(self) -> None:
        Path(self.database_path).parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as connection:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY,name TEXT NOT NULL,age INTEGER NOT NULL)"
            )

    def save(self, data: Data) -> None:
        try:
            with self._connect() as connection:
                connection.execute(
                    "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                    (data["name"], data["email"], data["age"]),
                )
        except sqlite3.IntegrityError as error:
            raise ValueError("duplicate email") from error

    def find_by_email(self, email: str) -> Data | None:
        with self._connect() as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.execute(
                """SELECT name, email, age FROM users WHERE email = ? """, (email,)
            )
            row = cursor.fetchone()

        if row is None:
            return None

        return {"name": row["name"], "email": row["email"], "age": row["age"]}
