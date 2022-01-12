import sqlite3

from links.link import Link
from util.blocked import Blocked


class Db:
    def __init__(self, database):
        self._database = database

    def insert(self, link: Link):
        block = link.block.value if link.block is not None else None
        self._cursor.execute("INSERT INTO link VALUES (?, ?, ?, ?, ?)",
                             (link.entrance, link.destination, link.one_way, block, link.note))

    def get(self, locations=None):
        if locations is None:
            self._cursor.execute("SELECT * FROM link")
        else:
            args = [locations[0] for locations in locations]
            self._cursor.execute('SELECT * FROM link WHERE entrance IN ({seq}) OR destination IN ({seq})'
                                 .format(seq=','.join(['?']*len(args))),
                                 args*2)
        return (self._convert(el) for el in self._cursor.fetchall())

    def get_by_keys(self, keys):
        self._cursor.execute('SELECT * FROM link WHERE entrance IN ({seq}) OR destination IN ({seq})'
                             .format(seq=','.join(['?']*len(keys))),
                             keys*2)
        return (self._convert(el) for el in self._cursor.fetchall())

    def get_from_entrance(self, key):
        self._cursor.execute("SELECT * FROM link WHERE entrance = (?) OR destination = (?)",
                             (key, key))
        element = self._cursor.fetchone()
        return self._convert(element) if element else None

    def remove_by_entrance(self, key):
        self._cursor.execute('DELETE FROM link WHERE entrance = (?) OR destination = (?)',
                             (key, key))

    def delete_all(self):
        self._cursor.execute('DELETE FROM link')

    @staticmethod
    def _convert(element):
        block = element[3]
        block = Blocked(int(block)) if block is not None else None
        note = element[4]
        note = note if note is not None else None
        return Link(element[0], element[1], element[2], block, note)

    def __enter__(self):
        self._conn = sqlite3.connect(self._database, isolation_level=None)
        self._cursor = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()
