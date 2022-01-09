from abc import abstractmethod, ABC

from PySide6.QtWidgets import QGridLayout, QLabel, QPushButton, QGroupBox

from util.gridutils import compute_cols, divide_widgets_per_column, create_grid


class ButtonGrid(QGroupBox):
    def __init__(self, elements, on_click, max_rows, title, initial):
        super().__init__(title)

        self.elements = elements
        self.on_click = on_click
        self.max_rows = max_rows

        self.buttons = QGridLayout(self)

        self.add_buttons(initial)

    def change_buttons(self, key):
        self.add_buttons(key)

    def add_buttons(self, initial):
        widgets = list(self.create_widgets(initial))
        columns = compute_cols(len(widgets), self.max_rows)

        division = divide_widgets_per_column(len(widgets), columns)
        grid = create_grid(widgets, list(division))
        for widget, (row, column) in grid:
            self.buttons.addWidget(widget, row, column)

    def create_button(self, key, name):
        button = QPushButton(name)
        button.clicked.connect(lambda: self.on_click(key))
        return button

    @abstractmethod
    def create_widgets(self, key):
        pass


class LocationGrid(ButtonGrid):
    def __init__(self, elements, on_click, max_rows):
        ButtonGrid.__init__(self, elements, on_click, max_rows, "Locations", None)

    def create_widgets(self, key):
        for category in self.elements.keys():
            yield QLabel(category.upper())
            for location_key, location_name in self.elements[category]:
                yield self.create_button(location_key, location_name)
            yield QLabel("================")


class ConnectionGrid(ButtonGrid):
    def __init__(self, elements, on_click, max_rows, initial_location):
        ButtonGrid.__init__(self, elements, on_click, max_rows, "Connections", initial_location)

    def create_widgets(self, location):
        elements = self.elements[location]
        for key, name in elements:
            yield self.create_button(key, name)
