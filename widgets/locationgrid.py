from PySide6.QtWidgets import QGridLayout, QLabel, QGroupBox

from util.button import create_button
from util.gridutils import compute_cols, divide_widgets_per_column, create_grid


class LocationGrid(QGroupBox):
    def __init__(self, elements, on_click, max_rows):
        super().__init__()
        self.elements = elements
        self.on_click = on_click
        self.max_rows = max_rows

        self.buttons = QGridLayout(self)
        self.add_buttons()

    def add_buttons(self):
        widgets = list(self._create_widgets())
        columns = compute_cols(len(widgets), self.max_rows)

        division = divide_widgets_per_column(len(widgets), columns)
        grid = create_grid(widgets, list(division))
        for widget, (row, column) in grid:
            self.buttons.addWidget(widget, row, column)

    def _create_widgets(self):
        for category in self.elements.keys():
            yield QLabel(category.upper())
            for location_key, location_name in self.elements[category]:
                yield create_button(location_key, location_name, self.on_click)
            yield QLabel("================")
