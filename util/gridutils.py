import math
from typing import List, Iterator


def compute_cols(n: int, max_rows: int):
    return math.ceil(n / max_rows)


def divide_widgets_per_column(widgets: int, columns: int) -> Iterator[int]:
    while widgets > 0:
        widgets_per_column = math.ceil(widgets / columns)
        yield widgets_per_column
        widgets -= widgets_per_column
        columns -= 1


def create_grid(widgets: dict, max_rows: int):
    columns = compute_cols(len(widgets), max_rows)

    division = divide_widgets_per_column(len(widgets), columns)
    return _create_grid_layout(list(widgets.values()), list(division))


def _create_grid_layout(widgets: List, division: List[float]):
    column, row = 0, 0
    while widgets:
        widget = widgets.pop(0)
        if row >= division[column]:
            row = 0
            column += 1
        yield widget, (row, column)
        row += 1
