from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout


class Locations(QGroupBox):
    def __init__(self, locations, set_location_callback):
        super().__init__("Cities")

        self.buttons = QVBoxLayout(self)
        self.set_location_callback = set_location_callback
        [self._add_city(key, name) for key, name in locations]

    def _add_city(self, key, name):
        button = self._create_button(key, name)
        self.buttons.addWidget(button)

    def _create_button(self, key, name):
        button = QPushButton(name)
        button.clicked.connect(lambda: self._set_location(key))
        return button

    def _set_location(self, location):
        self.set_location_callback(location)

