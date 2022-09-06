from dataclasses import dataclass, field
from datetime import datetime
from sqlite3 import Error, connect

from conf.paths import database_path


class DatabaseError(Error):
    pass


@dataclass
class Entry:
    title: str
    content: str
    date_created: str = field(default_factory=lambda: str(datetime.now()))


class DatabaseConnectionHandler:

    def __init__(self, db_path=database_path):
        self.conn = None
        self.db_path = db_path

    def __enter__(self):
        try:
            self.conn = connect(self.db_path)
        except DatabaseError:
            pass
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def add_entry(self, entry: Entry):
        self.conn.execute("INSERT INTO entries_entry (title, content, date_created)\n"
                          f"VALUES ('{entry.title}', '{entry.content}', '{entry.date_created}')")

    def read_entries(self):
        res = self.conn.execute("SELECT * FROM entries_entry")
        entries = list()
        for e in res.fetchall():
            entries.append(Entry(e.title, e.content, e.date_created))

    def update_entry(self, entry: Entry):
        self.conn.execute("UPDATE entries_entry\n"
                          f"SET title = {entry.title}, content = {entry.content}"
                          f"WHERE date_created = {entry.date_created}")

    def delete_entry(self, entry: Entry):
        self.conn.execute(f"DELETE FROM entries_entry WHERE date_created = {entry.date_created}")
