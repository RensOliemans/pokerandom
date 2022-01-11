import logging

from util.blocked import Blocked


class Link:
    def __init__(self, entrance, destination=None, one_way=False, block=None):
        self._assert_valid(entrance, destination, block)
        assert entrance is not None, 'Entrance cannot be None'
        assert destination is not None or destination is None and block is not None, 'If destination is None, a block' \
                                                                                     ' has to be given'
        self.entrance = entrance
        self.destination = destination
        self.one_way = one_way
        self.block = block

    @property
    def dead_end(self):
        return self.destination is None and self.block == Blocked.DEAD_END

    @property
    def blocked(self) -> bool:
        return self.destination is None

    def other(self, key):
        if key not in self:
            logging.error('Key %s was not found in link %s', key, self)
        if key == self.entrance:
            return self.destination
        return self.entrance

    @staticmethod
    def _assert_valid(entrance, destination, block):
        assert entrance is not None, 'Entrance cannot be None'
        assert (destination is not None and block is None) or (destination is None and block is not None), \
            'If destination is None, a block has to be given. If a destination is given, a block cannot be given.'

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
