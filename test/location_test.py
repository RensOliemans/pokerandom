import unittest

from widgets.locations import divide_widgets_per_column, create_grid


class TestGridAllocation(unittest.TestCase):
    def test_grid_allocation_basic(self):
        widgets = 8
        columns = 3
        division = divide_widgets_per_column(widgets, columns)
        expected = [
            (0, (0, 0)),
            (1, (1, 0)),
            (2, (2, 0)),
            (3, (0, 1)),
            (4, (1, 1)),
            (5, (2, 1)),
            (6, (0, 2)),
            (7, (1, 2)),
        ]
        self.assertEqual(expected, list(create_grid(list(range(widgets)), list(division))))

    def test_grid_allocation_whole(self):
        widgets = 10
        columns = 2
        division = divide_widgets_per_column(widgets, columns)
        expected = [
            (0, (0, 0)),
            (1, (1, 0)),
            (2, (2, 0)),
            (3, (3, 0)),
            (4, (4, 0)),
            (5, (0, 1)),
            (6, (1, 1)),
            (7, (2, 1)),
            (8, (3, 1)),
            (9, (4, 1)),
        ]
        self.assertEqual(expected, list(create_grid(list(range(widgets)), list(division))))


class TestGridDivision(unittest.TestCase):
    def test_grid_division_whole(self):
        n = 21
        c = 3
        expected = [7, 7, 7]
        self.assertEqual(expected, list(divide_widgets_per_column(n, c)))

    def test_grid_division_oneextra(self):
        n = 22
        c = 3
        expected = [8, 7, 7]
        self.assertEqual(expected, list(divide_widgets_per_column(n, c)))

    def test_grid_division_twoextra(self):
        n = 8
        c = 3
        expected = [3, 3, 2]
        self.assertEqual(expected, list(divide_widgets_per_column(n, c)))


if __name__ == '__main__':
    unittest.main()
