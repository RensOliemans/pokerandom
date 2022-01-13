import unittest

from util.locations import Category, Location, Entrance, get_entrances_of_category, get_name_of_key, \
    get_category_of_entrance, get_location_of_entrance, get_entrances_of_location

simple_categories = [
    Category('test', 'name', [
        Location('loc1', 'location 1', [
            Entrance('e1', 'E1'),
            Entrance('e2', 'E2')
        ]),
    ]),
]

medium_categories = [
    Category('test', 'name', [
        Location('loc1', 'location 1', [
            Entrance('e1', 'E1'),
            Entrance('e2', 'E2')
        ]),
        Location('loc2', 'location 2', [
            Entrance('e12', 'E12')
        ])
    ])
]

complex_categories = [
    Category('test', 'name', [
        Location('loc1', 'location 1', [
            Entrance('e1', 'E1'),
            Entrance('e2', 'E2')
        ]),
    ]),
    Category('second', 'Second', [
        Location('abc', 'ABC', [
            Entrance('entrance_1', 'Entrance 1'),
            Entrance('entrance_2', 'Entrance 2')
        ]),
        Location('def', 'DEF', [
            Entrance('entrance_12', 'Entrance 12')
        ])
    ]),
    Category('third', 'Second', [
        Location('ghi', 'GHI', [
            Entrance('entrance_4', 'Entrance 4')
        ]),
    ])
]


class TestGetKeysOfCategory(unittest.TestCase):
    def test_first_category(self):
        expected = [
            Entrance('e1', 'E1'),
            Entrance('e2', 'E2'),
            Entrance('e12', 'E12'),
        ]
        self.assertEqual(expected, list(get_entrances_of_category(medium_categories, 'test')))

    def test_complex_category(self):
        expected = [
            Entrance('entrance_1', 'Entrance 1'),
            Entrance('entrance_2', 'Entrance 2'),
            Entrance('entrance_12', 'Entrance 12'),
        ]
        self.assertEqual(expected, list(get_entrances_of_category(complex_categories, 'second')))


class TestGetKeysOfLocation(unittest.TestCase):
    def test_first_location(self):
        expected = [
            Entrance('e1', 'E1'),
            Entrance('e2', 'E2'),
        ]
        self.assertEqual(expected, list(get_entrances_of_location(medium_categories, 'loc1')))

    def test_middle_location(self):
        expected = [
            Entrance('entrance_1', 'Entrance 1'),
            Entrance('entrance_2', 'Entrance 2')
        ]
        self.assertEqual(expected, list(get_entrances_of_location(complex_categories, 'abc')))


class TestGetNameOfKey(unittest.TestCase):
    def test_get_name_of_first_key(self):
        expected = 'E1'
        self.assertEqual(expected, get_name_of_key(simple_categories, 'e1'))

    def test_get_name_of_later_key(self):
        expected = 'Entrance 12'
        self.assertEqual(expected, get_name_of_key(complex_categories, 'entrance_12'))


class TestGetCategoryOfEntrance(unittest.TestCase):
    def test_get_category_of_first_key(self):
        expected = simple_categories[0]
        self.assertEqual(expected, get_category_of_entrance(simple_categories, 'e1'))

    def test_get_category_of_later_key(self):
        expected = complex_categories[1]
        self.assertEqual(expected, get_category_of_entrance(complex_categories, 'entrance_12'))


class TestGetLocationOfEntrance(unittest.TestCase):
    def test_get_location_of_first_key(self):
        expected = simple_categories[0].locations[0]
        self.assertEqual(expected, get_location_of_entrance(simple_categories, 'e1'))

    def test_get_location_of_later_key(self):
        expected = complex_categories[1].locations[1]
        self.assertEqual(expected, get_location_of_entrance(complex_categories, 'entrance_12'))


if __name__ == '__main__':
    unittest.main()
