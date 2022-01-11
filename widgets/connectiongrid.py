from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QGridLayout, QGroupBox, QApplication

from util.button import create_button, EntranceButton
from util.gridutils import compute_cols, divide_widgets_per_column, create_grid
from util.widget import Widget


class ConnectionGrid(QGroupBox):
    def __init__(self, elements, on_click, on_ctrl_click, on_enter, on_leave, get_location_name, view_double, max_rows):
        super().__init__()

        self.elements = elements
        self.on_click = on_click
        self.on_ctrl_click = on_ctrl_click
        self.on_enter = on_enter
        self.on_leave = on_leave
        self.show_double = view_double
        self.max_rows = max_rows
        self.get_location_name = get_location_name

        self.selected = None
        self.double_information = None

        self.widgets: [Widget] = []
        self.buttons = QGridLayout(self)

    def set_buttons(self, key, links):
        self._remove_buttons()
        self._add_buttons(key, links)

    def show_destination(self, key):
        for widget in self.widgets:
            if widget.key == key:
                widget.widget.draw(active=True)

    def hide_destination(self, key):
        for widget in self.widgets:
            if widget.key == key:
                widget.widget.draw()

    def show_selected(self, key, selected):
        if not selected and self.selected is not None:
            self.selected.widget.draw()
        for widget in self.widgets:
            if widget.key == key:
                self.selected = widget
                widget.widget.draw(selected=True)

    def _remove_buttons(self):
        while self.widgets:
            widget = self.widgets.pop().widget
            self.buttons.removeWidget(widget)
            widget.deleteLater()
        self.selected = None

    def _add_buttons(self, location, links):
        widgets = list(self._create_widgets(location, links))
        columns = compute_cols(len(widgets), self.max_rows)

        division = divide_widgets_per_column(len(widgets), columns)
        grid = create_grid(widgets, list(division))
        for widget, (row, column) in grid:
            self.widgets.append(widget)
            self.buttons.addWidget(widget.widget, row, column)

    def _create_widgets(self, location, links):
        elements = self.elements[location]
        for key, name in elements:
            link = get_link_of_button(key, links)
            yield Widget(key, create_button(key, name, self.on_click, on_ctrl_click=self.on_ctrl_click,
                                            on_enter=self.on_enter, on_leave=self.on_leave, link=link,
                                            get_location_name=self.get_location_name))

    def show_double_connections(self):
        w = QApplication.widgetAt(QCursor.pos(self.screen()))
        if type(w) is EntranceButton:
            if not self.double_information == w.key:
                self.double_information = w.key
                self.show_double(self.double_information)
        else:
            self.double_information = None
            self.show_double(self.double_information)

    def hide_double_connections(self):
        if self.double_information is not None:
            self.double_information = None
            self.show_double(self.double_information)


def get_link_of_button(key, links):
    for link in links:
        if key in link:
            return link
