import time
from copy import copy, deepcopy

from PySide6.QtCore import (qVersion)
from PySide6.QtGui import (QGuiApplication, QIcon)
from PySide6.QtWidgets import *

from cities import CITIES


def class_name(o):
    return o.metaObject().className()


def init_widget(w, name):
    """Init a widget for the gallery, give it a tooltip showing the
       class name"""
    w.setObjectName(name)
    w.setToolTip(class_name(w))
    return w


class PokeRandom(QWidget):
    def __init__(self):
        super().__init__()

        self.current_city = CITIES[0][0]
        self.cities = self.create_cities(CITIES)
        self.notes = self.create_notes()

        self.left = QVBoxLayout()
        self.left.addWidget(self.cities)
        self.left.addWidget(self.notes)

        self.right = self.create_content()

        main_layout = QGridLayout(self)
        main_layout.addLayout(self.left, 0, 0)
        main_layout.addWidget(self.right, 0, 1)

        print(self.right)

        self.setWindowTitle("Pokémon Platinum Randomizer Tracker")

    def setVisible(self, visible):
        super(PokeRandom, self).setVisible(visible)

    def create_cities(self, cities):
        result = QGroupBox("Cities")
        init_widget(result, "buttons_groupbox")

        button_layout = QVBoxLayout(result)
        for name, key in cities:
            button = self._create_button(name, key)
            button_layout.addWidget(button)

        return result

    def _create_button(self, name, key):
        button = init_widget(QPushButton(name), key)
        button.clicked.connect(lambda: self._set_city(key))
        return button

    def create_notes(self):
        notes = init_widget(QToolBox(), "notes")

        plain_textedit = init_widget(QPlainTextEdit(""), "plainTextEdit")

        notes.addItem(plain_textedit, "Notes")
        return notes

    def create_content(self):
        viewer = init_widget(QToolBox(), "viewer")
        textedit = init_widget(QPlainTextEdit(""), "plainTextEdit")
        # textedit2 = init_widget(QPlainTextEdit(""), "plainTextEdit")

        viewer.addItem(textedit, self.current_city)
        # viewer.addItem(textedit2, self.current_city)
        return viewer

    def _set_city(self, city):
        print(city)
        self.current_city = city



