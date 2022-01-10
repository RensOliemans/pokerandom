from PySide6.QtWidgets import QGridLayout, QLabel, QGroupBox, QPushButton, QWidget

from util import colors
from util.button import create_button
from util.gridutils import compute_cols, divide_widgets_per_column, create_grid


class LocationGrid(QGroupBox):
    def __init__(self, elements, on_click, max_rows):
        super().__init__()
        self.elements = elements
        self.on_click = on_click
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
                widget.widget.setPalette(colors.default)

    def _create_widgets(self):
        for category in self.elements.keys():
            yield Widget('category', QLabel(category.upper()))
            for location_key, location_name in self.elements[category]:
                yield Widget(location_key,
                             create_button(location_key, location_name, self.on_click))
            yield Widget('hrule', QLabel('----------------'))


class Widget:
    def __init__(self, key, widget: QWidget):
        self.key = key
        self.widget = widget

    def __eq__(self, other):
        return (isinstance(other, Widget) and self.key == other.key
                or self.key == other)

    def __hash__(self):
        return hash(self.key)
