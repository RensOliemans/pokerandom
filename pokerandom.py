import logging

from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout

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

        self.locations = widgets.LocationGrid(
            locations, on_click=self.set_current_location, on_enter=self.show_connections,
            on_leave=self.hide_connections, max_rows=15
        )
        self.connections = widgets.ConnectionGrid(
            self.entrances, on_click=self.select_connection, on_ctrl_click=self._change_location_by_entrance,
            on_enter=self.show_connection, on_leave=self.hide_connection, get_location_name=self.get_name_of_location,
            view_double=self.show_double, max_rows=10
        )
        self.status = widgets.Status(self.selected, self.add_link, self.get_name_of_location)
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

    def _change_location_by_entrance(self, key):
        location = self.get_location_of_entrance(key)
        if location:
            self.set_current_location(location)

    def select_connection(self, location):
        self.status.select_item(location)

    def add_link(self, entrance, destination, one_way=False, block=None):
        self.link_manager.add_link(Link(entrance, destination, one_way, block))
        self.connections.set_buttons(self.current_location,
                                     self.link_manager.get_links(self.entrances[self.current_location]))

    def get_location_of_entrance(self, key):
        for category, entrances in self.entrances.items():
            if key in [entrance[0] for entrance in entrances]:
                return category

    def get_name_of_location(self, key):
        all_entrances = [self.entrances[x] for x in self.entrances.keys()]
        flattened = [i for sub in all_entrances for i in sub]
        try:
            return [x[1] for x in flattened if key == x[0]][0]
        except IndexError:
            logging.error('Could not find key %s, when I really expected it.', key)

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

    def selected(self, key, selected):
        self.connections.show_selected(key, selected)

    def setup_shortcuts(self):
        shortcuts = widgets.Shortcuts(self, self.status.cancel, self.status.oneway,
                                      self.status.blocked)

    def show_double(self, key):
        if key is None:
            self.locations.hide_second_destinations()
            return

        initial_link = self.link_manager.get_link(key)
        if initial_link is None:
            return

        destination = initial_link.other(key)
        if destination is None:
            return

        location = self.get_location_of_entrance(destination)
        destinations_of_destination = self.link_manager.get_links(self.entrances[location])
        for link in destinations_of_destination:
            loc = link.destination if self.get_location_of_entrance(link.entrance) == location else link.entrance

            self.locations.show_second_destination(self.get_location_of_entrance(loc))
