import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("./data/actors.db")
        self.table_name = "actors"

        self._connection.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            f"id INTEGER PRIMARY KEY AUTOINCREMENT, "
            f"first_name TEXT NOT NULL, "
            f"last_name TEXT NOT NULL"
            f")"

        )
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (format) VALUES (?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> None:
        cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(*row) for row in cursor
        ]

    def update(self, pk: str, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"UPDATR {self.table_name} "
            f"SET {first_name}, {last_name} = ? "
            f"WHERE {pk} = ? ",
            (pk, first_name, last_name),
        )
        self._connection.commit()

    def delete(self, pk: str) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE {pk} = ? ",
            (pk,)
        )
        self._connection.commit()
