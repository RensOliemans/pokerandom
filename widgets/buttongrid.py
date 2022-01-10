from PySide6.QtWidgets import QGridLayout, QGroupBox

from util.button import create_button
from util.gridutils import compute_cols, divide_widgets_per_column, create_grid


class ConnectionGrid(QGroupBox):
    def __init__(self, elements, on_click, on_enter, on_leave, max_rows):
        super().__init__()

        self.elements = elements
        self.on_click = on_click
        self.on_enter = on_enter
        self.on_leave = on_leave
        self.max_rows = max_rows

        self.widgets = []
        self.buttons = QGridLayout(self)

    def set_buttons(self, key, links):
        self._remove_buttons()
        self._add_buttons(key, links)

    def _remove_buttons(self):
        while self.widgets:
            widget = self.widgets.pop()
            self.buttons.removeWidget(widget)
            widget.deleteLater()

    def _add_buttons(self, location, links):
        widgets = list(self._create_widgets(location, links))
        columns = compute_cols(len(widgets), self.max_rows)

        division = divide_widgets_per_column(len(widgets), columns)
        grid = create_grid(widgets, list(division))
        for widget, (row, column) in grid:
            self.widgets.append(widget)
            self.buttons.addWidget(widget, row, column)

    def _create_widgets(self, location, links):
        elements = self.elements[location]
        for key, name in elements:
            link = get_link_of_button(key, links)
            yield create_button(key, name, self.on_click, self.on_enter, self.on_leave, link)


def get_link_of_button(key, links):
    for link in links:
        if key in link:
            return link
