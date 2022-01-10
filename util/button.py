from PySide6.QtCore import QEvent
from PySide6.QtGui import QPalette, QRgba64, QColor, QEnterEvent
from PySide6.QtWidgets import QPushButton

from util import colors


class LocationButton(QPushButton):
    def __init__(self, name, key, on_click, link=None):
        super().__init__(name)
        self.link = link

        self.clicked.connect(lambda: on_click(key))
        self.set_palette()

    def set_palette(self):
        if self.link is not None:
            self.setPalette(colors.existing_link)
        else:
            self.setPalette(colors.default)

    def enterEvent(self, event: QEnterEvent) -> None:
        self.setPalette(colors.hover)

    def leaveEvent(self, event: QEvent) -> None:
        self.set_palette()


def create_button(key, name, on_click, link=None):
    return LocationButton(name, key, on_click, link)


def on_hover(key, link, callback):
    if key == link.entrance:
        callback(link.destination)
    elif key == link.destination:
        callback(link.entrance)
