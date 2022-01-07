from PySide6.QtWidgets import *

from cities import CITIES
from citylist import CityList
from imageviewer import ImageViewer


class PokeRandom(QWidget):
    def __init__(self):
        super().__init__()

        self.current_city = CITIES[0][0]
        self.cities = CityList(CITIES, self.set_current_city)
        self.notes = self.create_notes()

        self.left = QVBoxLayout()
        self.left.addWidget(self.cities)
        self.left.addWidget(self.notes)

        self.image = ImageViewer(self.current_city)

        main_layout = QGridLayout(self)
        main_layout.addLayout(self.left, 0, 0)
        main_layout.addWidget(self.image, 0, 1)

        self.setWindowTitle("Pokémon Platinum Randomizer Tracker")

    def setVisible(self, visible):
        super(PokeRandom, self).setVisible(visible)

    def create_notes(self):
        notes = QToolBox()

        plain_textedit = QPlainTextEdit("")

        notes.addItem(plain_textedit, "Notes")
        return notes

    def set_current_city(self, city):
        self.current_city = city
        self.image.set_image(city)



