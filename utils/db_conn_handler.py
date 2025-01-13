from dataclasses import dataclass
from datetime import datetime

from django.db import connection


class DatabaseError(Exception):
    pass


@dataclass
class DatabaseEntry:
    title: str
    content: str

    @classmethod
    def new(cls):
        time = datetime.now().strftime("%Y-%m-%d %H:%M")
        return cls(f"New Test Entry: {time}", f"This was written at {time}")


class DatabaseConnectionHandler:

    @staticmethod
    def add_entry(entry: DatabaseEntry):
        with connection.cursor() as conn:
            conn.execute("INSERT INTO entries_entry (title, content, date_created)\n"
                         f"VALUES ('{entry.title}', '{entry.content}', '{datetime.now()}')")

    @staticmethod
    def read_entries() -> list[DatabaseEntry]:
        with connection.cursor() as conn:
            conn.execute("SELECT * FROM entries_entry")
            entries = list()
            for e in conn.fetchall():
                title, content = e[1], e[2]
                entry = DatabaseEntry(title, content)
                entries.append(entry)
        return entries

    @staticmethod
    def update_entry(entry: DatabaseEntry):
        with connection.cursor() as conn:
            conn.execute("UPDATE entries_entry\n"
                         f"SET content = '{entry.content}'"
                         f"WHERE title = '{entry.title}'")

    @staticmethod
    def delete_entry(entry: DatabaseEntry):
        with connection.cursor() as conn:
            conn.execute(f"DELETE FROM entries_entry WHERE title = '{entry.title}'")
