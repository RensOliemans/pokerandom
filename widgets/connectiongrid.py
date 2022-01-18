from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QGridLayout, QGroupBox, QApplication

from util.button import create_button, EntranceButton
from util.gridutils import create_grid
from util.locations import get_entrances_of_category, Entrance


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

        self.widgets: {Entrance: EntranceButton} = dict()
        self.buttons = QGridLayout(self)

    def set_buttons(self, key, links):
        self._remove_buttons()
        self._add_buttons(key, links)

    def show_destination(self, key):
        if key is not None and key in self.widgets:
            self.widgets[key].draw(active=True)

    def hide_destination(self, key):
        if key is not None and key in self.widgets:
            self.widgets[key].draw()

    def show_selected(self, entrance, selected):
        if not selected:
            self._hide_previously_selected()

        if entrance is not None and entrance.key in self.widgets:
            widget = self.widgets[entrance.key]
            self.selected = widget
            widget.draw(selected=True)

    def _hide_previously_selected(self):
        if self.selected is not None:
            self.selected.draw(selected=False)

    def _remove_buttons(self):
        for widget in self.widgets.values():
            self.buttons.removeWidget(widget)
            widget.deleteLater()
        self.widgets = dict()
        self.selected = None

    def _add_buttons(self, location, links):
        self._create_widgets(location, links)
        grid = create_grid(self.widgets, self.max_rows)
        for widget, (row, column) in grid:
            self.buttons.addWidget(widget, row, column)

    def _create_widgets(self, location, links):
        entrances = get_entrances_of_category(self.elements, location)
        for entrance in entrances:
            link = get_link_of_button(entrance.key, links)
            name = self._create_name(entrance, link)
            self.widgets[entrance.key] = create_button(entrance, self.on_click, on_ctrl_click=self.on_ctrl_click,
                                                       on_enter=self.on_enter, on_leave=self.on_leave, link=link, text=name)

    def _create_name(self, entrance, link):
        if not link or link.blocked:
            return entrance.name

        if link.has_note:
            return f'{entrance.name} — {link.note}'

        return f'{entrance.name} -> {self.get_location_name(link.other(entrance.key))}'

    def show_double_connections(self):
        w = QApplication.widgetAt(QCursor.pos(self.screen()))
        if type(w) is EntranceButton:
            if not self.double_information == w.entrance.key:
                self.double_information = w.entrance.key
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
