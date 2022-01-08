import math

from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QGridLayout, QLabel


class Locations(QGroupBox):
    def __init__(self, locations, change_location_callback):
        super().__init__("Cities")

        self.change_location_callback = change_location_callback
        self.buttons = QGridLayout(self)
        self.add_buttons(locations)

    def add_buttons(self, locations, columns=3):
        widgets = list(self._create_widgets(locations))

        division = divide_widgets_per_column(len(widgets), columns)
        grid = create_grid(widgets, list(division))
        for widget, (row, column) in grid:
            self.buttons.addWidget(widget, row, column)

    def _create_widgets(self, locations):
        for category in locations.keys():
            yield QLabel(category.upper())
            for location_key, location_name in locations[category]:
                yield self._create_button(location_key, location_name)
            yield QLabel("================")

    def _add_city(self, key, name):
        button = self._create_button(key, name)
        self.buttons.addWidget(button)

    def _create_button(self, key, name):
        button = QPushButton(name)
        button.clicked.connect(lambda: self._set_location(key))
        return button

    def _set_location(self, location):
        self.change_location_callback(location)


def divide_widgets_per_column(widgets, columns):
    while widgets > 0:
        widgets_per_column = math.ceil(widgets / columns)
        yield widgets_per_column
        widgets -= widgets_per_column
        columns -= 1


def create_grid(widgets, division):
    column, row = 0, 0
    while widgets:
        widget = widgets.pop(0)
        if row >= division[column]:
            row = 0
            column += 1
        yield widget, (row, column)
        row += 1
