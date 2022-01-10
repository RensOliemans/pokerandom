from PySide6.QtWidgets import QGridLayout, QLabel, QGroupBox, QPushButton, QWidget

from util import colors
from util.button import create_button
from util.gridutils import compute_cols, divide_widgets_per_column, create_grid
from util.widget import Widget


class LocationGrid(QGroupBox):
    def __init__(self, elements, on_click, on_enter, on_leave, max_rows):
        super().__init__()
        self.elements = elements
        self.on_click = on_click
        self.on_enter = on_enter
        self.on_leave = on_leave
        self.max_rows = max_rows
        self.widgets = list(self._create_widgets())

        self.buttons = QGridLayout(self)
        self.add_buttons()

    def add_buttons(self):
        columns = compute_cols(len(self.widgets), self.max_rows)

        division = divide_widgets_per_column(len(self.widgets), columns)
        grid = create_grid(self.widgets, list(division))
        for widget, (row, column) in grid:
            self.buttons.addWidget(widget.widget, row, column)

    def show_destination(self, key):
        for widget in self.widgets:
            if widget.key == key:
                widget.widget.setPalette(colors.linked)

    def hide_destination(self, key):
        for widget in self.widgets:
            if widget.key == key:
                widget.widget.setPalette(colors.light)

    def set_buttons(self, location, links, parent):
        self.clear_colors()
        locations = [parent(link.entrance) if parent(link.destination) == location else parent(link.destination)
                     for link in links]
        for widget in self.widgets:
            if widget.key in locations:
                widget.widget.setPalette(colors.light)

    def clear_colors(self):
        for widget in self.widgets:
            widget.widget.setPalette(colors.default)

    def _create_widgets(self):
        for category in self.elements.keys():
            yield Widget('category', QLabel(category.upper()))
            for location_key, location_name in self.elements[category]:
                yield Widget(location_key,
                             create_button(location_key, location_name, self.on_click, self.on_enter, self.on_leave))
            yield Widget('hrule', QLabel('----------------'))

