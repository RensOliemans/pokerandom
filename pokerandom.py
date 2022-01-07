from PySide6.QtWidgets import *

import widgets


class PokeRandom(QWidget):
    def __init__(self, cities, initial_city):
        super().__init__()
        self.setWindowTitle("Pokémon Platinum Randomizer Tracker")

        self.current_city = initial_city
        self.cities = widgets.CityList(cities, self.set_current_city)
        self.notes = widgets.Notes()

        self.image = widgets.ImageViewer(self.current_city)

        self.left = QVBoxLayout()
        self.left.addWidget(self.cities)
        self.left.addWidget(self.notes)

        main_layout = QGridLayout(self)
        main_layout.addLayout(self.left, 0, 0)
        main_layout.addWidget(self.image, 0, 1)

    def setVisible(self, visible):
        super(PokeRandom, self).setVisible(visible)

    def set_current_city(self, city):
        self.current_city = city
        self.image.set_image(city)



