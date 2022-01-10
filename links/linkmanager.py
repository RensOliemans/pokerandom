from links.db import Db
from links.link import Link


class LinkManager:
    def __init__(self, locations, entrances, database: Db):
        self.locations = locations
        self.entrances = entrances

        self.all_locations = flatten_dict(self.entrances)
        self.all_keys = {x[0] for x in self.all_locations}
        self._db = database

    def add_link(self, link: Link):
        self._check_valid_link(link)
        self._db.remove_by_entrance(link.entrance)
        self._db.remove_by_entrance(link.destination)
        self._db.insert(link)

    def get_links(self, keys=None):
        return list(self._db.get(keys))

    def get_link(self, key):
        return self._db.get_from_entrance(key)

    def _check_valid_link(self, link):
        if link.entrance not in self.all_keys:
            raise ValueError(f'{link.entrance} not in the known locations.')
        if not link.blocked and link.destination not in self.all_keys:
            raise ValueError(f'{link.destination} not in the known locations.')


def flatten_dict(d):
    sublists = [d[x] for x in d.keys()]
    return {i for sub in sublists for i in sub}
