import logging

from util.blocked import Blocked


class Link:
    def __init__(self, entrance, destination=None, one_way=False, block=None, note=None):
        self._assert_valid(entrance, destination, block, note)
        self.entrance = entrance
        self.destination = destination
        self.one_way = one_way
        self.block = block
        self.note = note

    @property
    def dead_end(self):
        return self.destination is None and self.block == Blocked.DEAD_END

    @property
    def blocked(self) -> bool:
        return self.destination is None and self.block is not None

    @property
    def has_note(self):
        return self.note is not None

    def other(self, entrance):
        if entrance not in self:
            logging.error('Key %s was not found in link %s', entrance, self)
        if entrance == self.entrance:
            return self.destination
        return self.entrance

    @staticmethod
    def _assert_valid(entrance, destination, block, note):
        assert entrance is not None, 'Entrance cannot be None'
        if destination is None:
            assert block is not None or note is not None, 'If destination is None, a block or note has to be given.'
        else:
            assert block is None, 'If a destination is given, a block cannot be given.'

    def __contains__(self, item):
        return item is not None and (item == self.entrance or item == self.destination)

    def __eq__(self, other):
        return (isinstance(other, Link) and (
            self.entrance == other.entrance and
            self.destination == other.destination))

    def __hash__(self):
        return hash((self.entrance, self.destination))

    def __repr__(self):
        if self.dead_end:
            return f"<Link from {self.entrance} ({self.block})>"
        else:
            return f"<Link from {self.entrance} to {self.destination}>"
