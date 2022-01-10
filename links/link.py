class Link:
    def __init__(self, entrance, destination=None):
        assert entrance is not None, 'Entrance cannot be None'
        self.entrance = entrance
        self.destination = destination

    @property
    def dead_end(self):
        return self.destination is None

    def other(self, key):
        assert key in self, f"key {key} not found in link {self}"
        if key == self.entrance:
            return self.destination
        return self.entrance

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
            return f"<Link from {self.entrance} (dead-end)>"
        else:
            return f"<Link from {self.entrance} to {self.destination}>"
