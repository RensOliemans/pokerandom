from PySide6.QtWidgets import *

import widgets


class PokeRandom(QWidget):
    def __init__(self, locations, initial_location, entrances):
        super().__init__()
        self.setWindowTitle("Pokémon Platinum Randomizer Tracker")

        self.current_location = initial_location
        self.entrances = entrances
        self.locations = widgets.LocationGrid(locations, self.change_current_location, 15)
        self.connections = widgets.ConnectionGrid(self.entrances, self.select_connection, 10, self.current_location[0])
        self.status = widgets.Status(self.add_link, self.get_name_of_location)

        self.image = widgets.ImageViewer(self.current_location[0])

        self.left = QVBoxLayout()
        self.left.addWidget(self.locations)
        self.left.addWidget(self.connections)
        self.left.addWidget(self.status)

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
        self.status.select_item(location)

    def add_link(self, entrance, destination):
        print(f'Added link between {entrance} and {destination}')

    def get_name_of_location(self, key):
        all_entrances = [self.entrances[x] for x in self.entrances.keys()]
        flattened = [i for sub in all_entrances for i in sub]
        return [x[1] for x in flattened if key == x[0]][0]



