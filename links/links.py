from links.db import Db
from links.link import Link


class Links(set):
    def __init__(self, db: Db):
        super().__init__()
        self._db = db

    def add(self, link: Link) -> None:
        super(Links, self).add(link)
        self._db.insert(link)
