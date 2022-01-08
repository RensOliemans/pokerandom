from PySide6.QtWidgets import *

import widgets


class PokeRandom(QWidget):
    def __init__(self, locations, initial_location):
        super().__init__()
        self.setWindowTitle("Pokémon Platinum Randomizer Tracker")

        self.current_location = initial_location
        self.locations = widgets.Locations(locations, self.set_current_location)
        self.notes = widgets.Notes()

        self.image = widgets.ImageViewer(self.current_location)

        self.left = QVBoxLayout()
        self.left.addWidget(self.locations)
        self.left.addWidget(self.notes)

        main_layout = QGridLayout(self)
        main_layout.addLayout(self.left, 0, 0)
        main_layout.addWidget(self.image, 0, 1)

    def setVisible(self, visible):
        super(PokeRandom, self).setVisible(visible)

    def set_current_location(self, location):
        self.current_location = location
        self.image.set_image(location)



