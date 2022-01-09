from PySide6.QtWidgets import QGroupBox, QGridLayout

from util.gridutils import compute_cols, divide_widgets_per_column, create_grid


class Connections(QGroupBox):
    def __init__(self, connections, current_location, max_rows=10):
        super().__init__("Connections")

        self.connections = connections
        self.max_rows = max_rows
        self.buttons = QGridLayout()

        self.change_connections(current_location)

    def change_connections(self, location):
        connections = self.connections[location]
        columns = compute_cols(len(connections), self.max_rows)

        division = divide_widgets_per_column(len(connections), columns)
        grid = create_grid(connections, list(division))
        for widget, (row, column) in grid:
            self.buttons.addWidget(widget, row, column)
