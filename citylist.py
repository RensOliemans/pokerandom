from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout


class CityList(QGroupBox):
    def __init__(self, cities, set_city):
        super().__init__("Cities")

        self.buttons = QVBoxLayout(self)
        self.set_city = set_city
        [self._add_city(key, name) for key, name in cities]

    def _add_city(self, key, name):
        button = self._create_button(key, name)
        self.buttons.addWidget(button)

    def _create_button(self, key, name):
        button = QPushButton(name)
        button.clicked.connect(lambda: self._set_city(key))
        return button

    def _set_city(self, city):
        print(city)
        self.set_city(city)

