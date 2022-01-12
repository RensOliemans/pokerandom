from PySide6.QtWidgets import QGridLayout, QLabel, QGroupBox, QPushButton, QWidget

from util import colors
from util.button import create_button
from util.gridutils import compute_cols, divide_widgets_per_column, create_grid
from util.widget import Widget


class LocationGrid(QGroupBox):
    def __init__(self, elements, on_click, on_enter, on_leave, get_parent, max_rows):
        super().__init__()

        self.elements = elements
        self.on_click = on_click
        self.on_enter = on_enter
        self.on_leave = on_leave
        self.get_parent = get_parent
        self.max_rows = max_rows

        self.location = None
        self.links = None

        self.widgets: [Widget] = []
        self.buttons = QGridLayout(self)
        self._add_buttons()

    def change_location(self, location, links):
        self.location = location
        self.links = links
        self.set_buttons()

    def set_buttons(self):
        self._clear_colors()
        locations = [self.get_parent(link.entrance)
                     if self.get_parent(link.destination) == self.location else self.get_parent(link.destination)
                     for link in self.links]
        for widget in self.widgets:
            if widget.key in locations:
                widget.widget.setPalette(colors.existing_link)

    def show_destination(self, key):
        if key is None:
            return

        widgets_to_change = [w for w in self.widgets if w.key == key]
        for widget in widgets_to_change:
            widget.widget.setPalette(colors.linked)

    def show_second_destination(self, key):
        self.show_destination(key)

    def _add_buttons(self):
        self.widgets = list(self._create_widgets())
        columns = compute_cols(len(self.widgets), self.max_rows)

        division = divide_widgets_per_column(len(self.widgets), columns)
        grid = create_grid(self.widgets, list(division))
        for widget, (row, column) in grid:
            self.buttons.addWidget(widget.widget, row, column)

    def _clear_colors(self):
        for widget in self.widgets:
            widget.widget.setPalette(colors.default)

    def _create_widgets(self):
        for category in self.elements.keys():
            for location_key, location_name in self.elements[category]:
                yield Widget(location_key,
                             create_button(location_key, location_name, self.on_click,
                                           on_enter=self.on_enter, on_leave=self.on_leave))

