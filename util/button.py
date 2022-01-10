from PySide6.QtCore import QEvent
from PySide6.QtGui import QEnterEvent
from PySide6.QtWidgets import QPushButton

from util import colors


class EntranceButton(QPushButton):
    def __init__(self, name, key, on_click, on_hover=None, link=None):
        super().__init__(name)
        self.key = key
        self.link = link
        self.on_hover = on_hover

        self.clicked.connect(lambda: on_click(key))
        self.set_palette()

    def set_palette(self):
        if self.link is not None:
            self.setPalette(colors.existing_link)
        else:
            self.setPalette(colors.default)

    def enterEvent(self, event: QEnterEvent) -> None:
        if self.on_hover:
            self.on_hover(self.key)

    def leaveEvent(self, event: QEvent) -> None:
        self.set_palette()


def create_button(key, name, on_click, on_hover=None, link=None):
    return EntranceButton(name, key, on_click, on_hover, link)
