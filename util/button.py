from PySide6.QtCore import QEvent
from PySide6.QtGui import QEnterEvent, QMouseEvent, Qt
from PySide6.QtWidgets import QPushButton

from util import colors, stylesheets
from util.blocked import Blocked


class EntranceButton(QPushButton):
    def __init__(self, key, name, on_click, on_ctrl_click=None, on_enter=None, on_leave=None, link=None,
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
            self.change_color(colors.existing_link, stylesheet=stylesheets.selected,
                              tooltip='Click on another location to link it to this one.')
        elif self.link is None:
            self.change_color(colors.default)
        elif self.link.blocked:
            self.draw_blocked()
        elif active:
            self.change_color(colors.linked)
        elif self.link.has_note:
            self.change_color(colors.note)
        else:
            self.change_color(colors.existing_link, tooltip=self.get_location_name(self.link.other(self.key)))

    def draw_blocked(self):
        if self.link.dead_end:
            self.change_color(colors.dead_end, stylesheet=stylesheets.blocked, tooltip='Dead end')
            return

        block = self.link.block
        color = None
        if block == Blocked.CUT:
            color = colors.cut
        elif block == Blocked.ROCK_SMASH:
            color = colors.rock_smash
        elif block == Blocked.STRENGTH:
            color = colors.strength
        elif block == Blocked.SURF:
            color = colors.surf
        elif block == Blocked.WATERFALL:
            color = colors.waterfall
        elif block == Blocked.ROCK_CLIMB:
            color = colors.rock_climb
        elif block == Blocked.TRAINER:
            color = colors.trainer
        elif block == Blocked.EVENT:
            color = colors.event
        self.change_color(color, tooltip=f'Blocked by {block}')

    def change_color(self, color, *, stylesheet=None, tooltip=None):
        self.setStyleSheet('' if stylesheet is None else stylesheet)
        self.setPalette(color)
        if tooltip:
            self.setToolTip(tooltip)

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
    return EntranceButton(key, name, on_click, on_ctrl_click, on_enter, on_leave, link, get_location_name)
