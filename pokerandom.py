from PySide6.QtWidgets import *

import widgets


class PokeRandom(QWidget):
    def __init__(self, locations, initial_location, entrances):
        super().__init__()
        self.setWindowTitle("Pokémon Platinum Randomizer Tracker")

        self.current_location = initial_location
        self.locations = widgets.LocationGrid(locations, self.change_current_location, 15)
        self.connections = widgets.ConnectionGrid(entrances, self.select_connection, 10, self.current_location[0])
        self.notes = widgets.Notes()

        self.image = widgets.ImageViewer(self.current_location[0])

        self.left = QVBoxLayout()
        self.left.addWidget(self.locations)
        self.left.addWidget(self.connections)
        self.left.addWidget(self.notes)

        main_layout = QGridLayout(self)
        main_layout.addLayout(self.left, 0, 0)
        main_layout.addWidget(self.image, 0, 1)

    def setVisible(self, visible):
        super(PokeRandom, self).setVisible(visible)

    def change_current_location(self, location):
        self.current_location = location
        self.image.set_image(location)
        self.connections.change_buttons(location)

    def select_connection(self, location):
        print(location)



