from links.db import Db
from links.link import Link
from util.locations import Category


class LinkManager:
    def __init__(self, categories, database: Db):
        self.categories = categories

        self.all_locations = flatten_dict(self.categories)
        self.all_keys = {x.key for x in self.all_locations}
        self._db = database

    def add_link(self, link: Link):
        self._check_valid_link(link)
        self._db.remove_by_entrance(link.entrance)
        self._db.remove_by_entrance(link.destination)
        self._db.insert(link)

    def get_links(self, locations=None):
        return list(self._db.get(locations))

    def get_links_by_keys(self, keys):
        return list(self._db.get_by_keys(keys))

    def get_link(self, key):
        if key is not None:
            return self._db.get_from_entrance(key)

    def _check_valid_link(self, link):
        if link.entrance not in self.all_keys:
            raise ValueError(f'{link.entrance} not in the known locations.')
        if not link.note and not link.blocked and link.destination not in self.all_keys:
            raise ValueError(f'{link.destination} not in the known locations.')


def flatten_dict(d: [Category]):
    entrances = [loc.entrances for sub in d for loc in sub.locations]
    return {i for sub in entrances for i in sub}
