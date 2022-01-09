from PySide6.QtWidgets import QGroupBox


class Connections(QGroupBox):
    def __init__(self, entrances, current_location, max_rows=10):
        super().__init__("Connections")

        self.entrances = entrances
        self.change_entrances(current_location)
        self.max_rows = max_rows

    def change_entrances(self, location):
        self

