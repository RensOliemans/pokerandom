from PySide6.QtCore import QEvent
from PySide6.QtGui import QEnterEvent
from PySide6.QtWidgets import QPushButton

from util import colors
from util.blocked import Blocked


class EntranceButton(QPushButton):
    def __init__(self, name, key, on_click, on_enter=None, on_leave=None, link=None):
        super().__init__(name)
        self.key = key
        self.link = link
        self.on_enter = on_enter
        self.on_leave = on_leave

        self.clicked.connect(lambda: on_click(key))
        self.draw()

    def draw(self, active=False):
        if self.link is None:
            self.setPalette(colors.default)
            return

        if self.link.dead_end:
            self.draw_dead_end()
            return

        if active:
            self.setPalette(colors.linked)
        else:
            self.setPalette(colors.existing_link)

    def draw_dead_end(self):
        if self.link.dead_end:
            self.setStyleSheet('QWidget { text-decoration: line-through; }')
            self.setPalette(colors.dead_end)
            return

        blocked = self.link.blocked
        if blocked == Blocked.ROCK_SMASH:
            self.setPalette(colors.rock_smash)
        elif blocked == Blocked.STRENGTH:
            self.setPalette(colors.strength)
        elif blocked == Blocked.SURF:
            self.setPalette(colors.surf)
        elif blocked == Blocked.WATERFALL:
            self.setPalette(colors.waterfall)

    def enterEvent(self, event: QEnterEvent) -> None:
        if self.on_enter:
            self.on_enter(self.key)

    def leaveEvent(self, event: QEvent) -> None:
        if self.on_leave:
            self.on_leave(self.key)


def create_button(key, name, on_click, on_hover=None, on_leave=None, link=None):
    return EntranceButton(name, key, on_click, on_hover, on_leave, link)
