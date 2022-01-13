class Category:
    """
    A group of locations that together forms 1 unit, for example 'Places of Interest'. These are not necessarily
    logically linked, but are grouped together for visual reasons.
    """

    def __init__(self, key, name, locations):
        self.key = key
        self.name = name
        self.locations = locations


class Location:
    """
    A logically connected group of entrances. From each of these entrances, you can warp
     to every other entrance in-game.
    """

    def __init__(self, key, name, entrances):
        self.key = key
        self.name = name
        self.entrances = entrances

    def __eq__(self, other):
        return (isinstance(other, Location)
                and self.key == other.key and self.name == other.name)


class Entrance:
    def __init__(self, key, name):
        self.key = key
        self.name = name

    def __eq__(self, other):
        return (isinstance(other, Entrance)
                and self.key == other.key and self.name == other.name)

    def __hash__(self):
        return hash((self.key, self.name))


def get_entrances_of_category(categories, key):
    category = [x for x in categories if x.key == key][0]
    return _get_entrances_of_locations(category.locations)


def get_entrances_of_location(categories, key):
    for category in categories:
        for location in category.locations:
            if location.key == key:
                return _get_entrances_of_locations([location])


def get_name_of_key(categories, key):
    for category in categories:
        for location in category.locations:
            for entrance in location.entrances:
                if entrance.key == key:
                    return entrance.name


def get_category_of_entrance(categories, key):
    for category in categories:
        for location in category.locations:
            if key in [e.key for e in location.entrances]:
                return category


def get_location_of_entrance(categories, key):
    for category in categories:
        for location in category.locations:
            if key in [e.key for e in location.entrances]:
                return location


def _get_entrances_of_locations(locations):
    for loc in locations:
        for entrance in loc.entrances:
            yield entrance
