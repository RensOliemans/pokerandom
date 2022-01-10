import sqlite3

from links.link import Link


class Db:
    def __init__(self, database):
        self._database = database

    def insert(self, link: Link):
        self._cursor.execute("INSERT INTO link VALUES (?, ?)",
                             (link.entrance, link.destination))

    def get(self, keys=None):
        if keys is None:
            self._cursor.execute("SELECT * FROM link")
        else:
            args = [key[0] for key in keys]
            self._cursor.execute('SELECT * FROM link WHERE entrance IN ({seq}) OR destination IN ({seq})'
                                 .format(seq=','.join(['?']*len(args))),
                                 args*2)
        return (Link(el[0], el[1]) for el in self._cursor.fetchall())

    def get_from_entrance(self, key):
        self._cursor.execute("SELECT * FROM link WHERE entrance = (?) OR destination = (?)",
                             (key, key))
        link = self._cursor.fetchone()
        return Link(link[0], link[1]) if link else None

    def remove_by_entrance(self, key):
        self._cursor.execute('DELETE FROM link WHERE entrance = (?) OR destination = (?)',
                             (key, key))

    def delete_all(self):
        self._cursor.execute('DELETE FROM link')

    def __enter__(self):
        self._conn = sqlite3.connect(self._database, isolation_level=None)
        self._cursor = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()
