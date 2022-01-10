from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLayout

import widgets
from links.link import Link
from links.linkmanager import LinkManager


class PokeRandom(QWidget):
    def __init__(self, locations, initial_location, entrances, db):
        super().__init__()
        self.setWindowTitle("Pokémon Platinum Randomizer Tracker")

        self.link_manager = LinkManager(locations, entrances, db)
        self.current_location = initial_location[0]
        self.entrances = entrances

        self._highlighting_entrances = []

        self.locations = widgets.LocationGrid(locations, self.set_current_location,
                                              self.show_connections, self.hide_connections, 15)
        self.connections = widgets.ConnectionGrid(self.entrances, self.select_connection,
                                                  self.show_connection, self.hide_connection, 10)
        self.status = widgets.Status(self.add_link, self.get_name_of_location)
        self.image = widgets.ImageViewer(max_height=800, max_width=800)

        self.set_current_location(self.current_location)

        self.setup_shortcuts()

        self.left = QVBoxLayout()
        self.left.addWidget(self.locations)
        self.left.addWidget(self.connections)

        main_layout = QGridLayout(self)
        main_layout.addLayout(self.left, 1, 0)
        main_layout.addWidget(self.status, 0, 1)
        main_layout.addWidget(self.image, 1, 1)

    def setVisible(self, visible):
        super(PokeRandom, self).setVisible(visible)

    def set_current_location(self, location):
        self.current_location = location
        self.image.set_image(location)
        links = self.link_manager.get_links(self.entrances[location])
        self.locations.set_buttons(location, links, self.get_location_of_entrance)
        self.connections.set_buttons(location, links)

    def select_connection(self, location):
        self.status.select_item(location)

    def add_link(self, entrance, destination):
        self.link_manager.add_link(Link(entrance, destination))
        self.connections.set_buttons(self.current_location,
                                     self.link_manager.get_links(self.entrances[self.current_location]))

    def get_location_of_entrance(self, key):
        for category, entrances in self.entrances.items():
            if key in [entrance[0] for entrance in entrances]:
                return category

    def get_name_of_location(self, key):
        all_entrances = [self.entrances[x] for x in self.entrances.keys()]
        flattened = [i for sub in all_entrances for i in sub]
        return [x[1] for x in flattened if key == x[0]][0]

    def show_connection(self, key):
        link = self.link_manager.get_link(key)
        if link:
            destination = link.other(key)
            self.locations.show_destination(self.get_location_of_entrance(destination))
            self.connections.show_destination(destination)

    def hide_connection(self, key):
        link = self.link_manager.get_link(key)
        if link:
            destination = link.other(key)
            self.locations.hide_destination(self.get_location_of_entrance(destination))
            self.connections.hide_destination(destination)

    def show_connections(self, key):
        self._highlighting_entrances = self.link_manager.get_links(self.entrances[key])
        for link in self._highlighting_entrances:
            if self.get_location_of_entrance(link.entrance) == key:
                self.connections.show_destination(link.destination)
            if self.get_location_of_entrance(link.destination) == key:
                self.connections.show_destination(link.entrance)

    def hide_connections(self, key):
        for link in self._highlighting_entrances:
            self.connections.hide_destination(link.destination)
            self.connections.hide_destination(link.entrance)

    def setup_shortcuts(self):
        shortcuts = widgets.Shortcuts(self, self.status.cancel)

