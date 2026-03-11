import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)

    def create(self, first_name, last_name):
        self.connection.execute(
            f"INSERT INTO {self.table_name} "
            f"VALUES (?, ?)",
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self):
        all_inform_from_db = self.connection.execute(
            f"SELECT *"
            f"FROM {self.table_name}"
        )
        return [row for row in all_inform_from_db]

    def update(self, pk: int,
               new_first_name: str,
               new_last_name: str):
        self.connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE pk = ?",
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    def delete(self, pk: int):
        self.connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE pk = ?",
            (pk,)
        )
        self.connection.commit()

# if __name__ == "__main__":
#     manager = ActorManager("test", "test")
#     print(manager.all())