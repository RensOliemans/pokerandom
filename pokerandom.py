import logging

from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout

import widgets
from links.link import Link
from links.linkmanager import LinkManager
from util.locations import get_entrances_of_category, get_name_of_key, get_category_of_entrance, \
    get_location_of_entrance, get_entrances_of_location


class PokeRandom(QWidget):
    def __init__(self, categories, initial_location, db):
        super().__init__()
        self.setWindowTitle("Pokémon Platinum Randomizer Tracker")

        self.link_manager = LinkManager(categories, db)
        self.current_location = initial_location
        self.entrances = categories

        self._highlighting_entrances = []

        self.locations = widgets.LocationGrid(
            categories, on_click=self.set_current_location, on_enter=self.show_connections,
            on_leave=self.hide_connections, get_parent=self.get_category_of_entrance, max_rows=15
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

        self.help = widgets.Help()
        self.small_help = widgets.SmallHelp(self)

        self.left = QVBoxLayout()
        self.left.addWidget(self.locations)
        self.left.addWidget(self.connections)

        main_layout = QGridLayout(self)
        main_layout.addWidget(self.small_help, 0, 0)
        main_layout.addLayout(self.left, 1, 0)
        main_layout.addWidget(self.status, 0, 1)
        main_layout.addWidget(self.image, 1, 1)

    def setVisible(self, visible):
        super(PokeRandom, self).setVisible(visible)

    def set_current_location(self, location):
        self.current_location = location.key
        self.image.set_image(self.current_location)
        self.redraw_location()

    def redraw_location(self):
        links = self.link_manager.get_links(self.get_entrances_of_category())
        self.locations.change_location(self.current_location, links)
        self.connections.set_buttons(self.current_location, links)

    def select_connection(self, location):
        self.status.select_item(location)

    def add_link(self, entrance, destination, one_way=False, block=None, note=None):
        self.link_manager.add_link(Link(entrance, destination, one_way, block, note))
        self.redraw_location()

    def get_name_of_location(self, key):
        return get_name_of_key(self.entrances, key)

    def get_location_of_entrance(self, key):
        return get_location_of_entrance(self.entrances, key)

    def get_category_of_entrance(self, key):
        return get_category_of_entrance(self.entrances, key)

    def show_connection(self, entrance):
        destination = self._get_destination(entrance.key)

        self.locations.show_destination(self.get_category_of_entrance(destination))
        self.connections.show_destination(destination)

    def hide_connection(self, entrance):
        destination = self._get_destination(entrance.key)

        self.locations.set_buttons()
        self.connections.hide_destination(destination)

    def show_connections(self, category):
        key = category.key
        self._highlighting_entrances = self.link_manager.get_links(self.get_entrances_of_category(key))
        for link in self._highlighting_entrances:
            if self.get_category_of_entrance(link.entrance).key == key:
                self.connections.show_destination(link.destination)

            destination = self.get_category_of_entrance(link.destination)
            if destination is None:
                return

            if destination.key == key:
                self.connections.show_destination(link.entrance)

    def hide_connections(self, key):
        for link in self._highlighting_entrances:
            self.connections.hide_destination(link.destination)
            self.connections.hide_destination(link.entrance)

    def selected(self, key, selected):
        self.connections.show_selected(key, selected)

    def setup_shortcuts(self):
        shortcuts = widgets.Shortcuts(self, self.status.cancel, self.status.oneway, self.status.show_note,
                                      self.status.blocked, self.show_help)

    def show_double(self, key):
        if key is None:
            self.locations.set_buttons()
            return

        initial_link = self.link_manager.get_link(key)
        if initial_link is None:
            return

        destination = initial_link.other(key)
        if destination is None:
            return

        location = self.get_location_of_entrance(destination)
        destinations_of_destination = self.link_manager.get_links(self.get_entrances_of_location(location.key))
        for link in destinations_of_destination:
            loc = link.destination if self.get_location_of_entrance(link.entrance) == location else link.entrance

            self.locations.show_destination(self.get_category_of_entrance(loc))

    def _change_location_by_entrance(self, key):
        location = self.get_category_of_entrance(key)
        if location:
            self.set_current_location(location)

    def _get_destination(self, key):
        link = self.link_manager.get_link(key)
        return link.other(key) if link is not None else None

    def get_entrances_of_category(self, key=None):
        if key is None:
            key = self.current_location
        return get_entrances_of_category(self.entrances, key)

    def get_entrances_of_location(self, key):
        return get_entrances_of_location(self.entrances, key)

    def show_help(self):
        self.help.show()
