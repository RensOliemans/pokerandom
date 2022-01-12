from PySide6.QtCore import QEvent
from PySide6.QtGui import QEnterEvent, QMouseEvent, Qt
from PySide6.QtWidgets import QPushButton

from util import colors
from util.blocked import Blocked


class EntranceButton(QPushButton):
    def __init__(self, name, key, on_click, on_ctrl_click=None, on_enter=None, on_leave=None, link=None,
                 get_location_name=None):
        super().__init__(name)
        self.key = key
        self.link = link
        self.on_click = on_click
        self.on_ctrl_click = on_ctrl_click
        self.on_enter = on_enter
        self.on_leave = on_leave
        self.get_location_name = get_location_name

        self.clicked.connect(lambda: self.call(key))
        self.draw()

    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.modifiers() == Qt.ControlModifier and self.on_ctrl_click is not None:
            return self.on_ctrl_click(self.link.other(self.key))

        super().mousePressEvent(e)

    def call(self, key):
        self.on_leave(key)
        self.on_click(key)

    def draw(self, active=False, selected=False):
        if selected:
            self.setToolTip('Click on another location to link it to this one.')
            self.setStyleSheet('QWidget { text-decoration: underline; }')
            self.setPalette(colors.existing_link)
        elif self.link is None:
            self.setStyleSheet('')
            self.setPalette(colors.default)
        elif self.link.blocked:
            self.draw_blocked()
        elif active:
            self.setPalette(colors.linked)
        else:
            self.setToolTip(self.get_location_name(self.link.other(self.key)))
            self.setPalette(colors.existing_link)

    def draw_blocked(self):
        if self.link.dead_end:
            self.setToolTip(f'Dead end')
            self.setStyleSheet('QWidget { text-decoration: line-through; }')
            self.setPalette(colors.dead_end)
            return

        block = self.link.block
        if block == Blocked.CUT:
            self.setPalette(colors.cut)
        elif block == Blocked.ROCK_SMASH:
            self.setPalette(colors.rock_smash)
        elif block == Blocked.STRENGTH:
            self.setPalette(colors.strength)
        elif block == Blocked.SURF:
            self.setPalette(colors.surf)
        elif block == Blocked.WATERFALL:
            self.setPalette(colors.waterfall)
        elif block == Blocked.ROCK_CLIMB:
            self.setPalette(colors.rock_climb)
        elif block == Blocked.TRAINER:
            self.setPalette(colors.trainer)
        elif block == Blocked.EVENT:
            self.setPalette(colors.event)
        self.setToolTip(f'Blocked by {block}')

    def enterEvent(self, event: QEnterEvent) -> None:
        if self.on_enter:
            self.on_enter(self.key)

    def leaveEvent(self, event: QEvent) -> None:
        if self.on_leave:
            self.on_leave(self.key)

    def __repr__(self):
        return f"<EntranceButton({self.key})>"


def create_button(key, name, on_click, *, on_ctrl_click=None, on_enter=None, on_leave=None, link=None,
                  get_location_name=None):
    return EntranceButton(name, key, on_click, on_ctrl_click, on_enter, on_leave, link, get_location_name)
