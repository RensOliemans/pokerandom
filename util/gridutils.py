import math
import copy


def compute_cols(n, max_rows):
    return math.ceil(n / max_rows)


def divide_widgets_per_column(widgets, columns):
    while widgets > 0:
        widgets_per_column = math.ceil(widgets / columns)
        yield widgets_per_column
        widgets -= widgets_per_column
        columns -= 1


def create_grid(widgets, division):
    widgets = copy.copy(widgets)
    column, row = 0, 0
    while widgets:
        widget = widgets.pop(0)
        if row >= division[column]:
            row = 0
            column += 1
        yield widget, (row, column)
        row += 1
