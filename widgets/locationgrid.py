from PySide6.QtWidgets import QGridLayout, QGroupBox

from util import colors
from util.button import create_button
from util.gridutils import create_grid


class LocationGrid(QGroupBox):
    def __init__(self, elements, on_click, on_enter, on_leave, get_parent, max_rows):
        super().__init__()

        self.categories = elements
        self.on_click = on_click
        self.on_enter = on_enter
        self.on_leave = on_leave
        self.get_parent = get_parent
        self.max_rows = max_rows

        self.location = None
        self.links = None

        self.widgets = dict()
        self.buttons = QGridLayout(self)
        self._add_buttons()

    def set_buttons(self):
        self._clear_colors()
        self._redraw_widgets()

    def change_location(self, location, links):
        self.location = location
        self.links = links
        self.set_buttons()

    def show_destination(self, category):
        if category is None:
            return

        self.widgets[category.key].setPalette(colors.linked)

    def _clear_colors(self):
        for widget in self.widgets.values():
            widget.setPalette(colors.default)

    def _redraw_widgets(self):
        categories = self._get_linked_categories()
        for category in categories:
            if category is None:
                continue
            self.widgets[category.key].setPalette(colors.existing_link)

    def _add_buttons(self):
        self._create_widgets()
        grid = create_grid(self.widgets, self.max_rows)
        for widget, (row, column) in grid:
            self.buttons.addWidget(widget, row, column)

    def _create_widgets(self):
        self.widgets = {
            category.key: create_button(category, self.on_click, on_enter=self.on_enter,
                                        on_leave=self.on_leave)
            for category in self.categories
        }

    def _get_linked_categories(self):
        for link in self.links:
            dest_parent = self.get_parent(link.destination)
            if dest_parent and dest_parent.key == self.location:
                yield self.get_parent(link.entrance)
            else:
                yield self.get_parent(link.destination)
