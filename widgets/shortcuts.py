from PySide6.QtGui import QShortcut, QKeySequence

from util.blocked import Blocked


class Shortcuts:
    def __init__(self, parent, cancel, one_way, blocked):
        self.parent = parent

        self._add_shortcut('q', cancel)
        self._add_shortcut('1', one_way)

        dead_end = lambda: blocked(Blocked.DEAD_END)
        self._add_shortcut('d', dead_end)

        rock_smash = lambda: blocked(Blocked.ROCK_SMASH)
        self._add_shortcut('r', rock_smash)

        strength = lambda: blocked(Blocked.STRENGTH)
        self._add_shortcut('s', strength)

        surf = lambda: blocked(Blocked.SURF)
        self._add_shortcut('f', surf)

        waterfall = lambda: blocked(Blocked.WATERFALL)
        self._add_shortcut('w', waterfall)

        trainer = lambda: blocked(Blocked.TRAINER)
        self._add_shortcut('t', trainer)

        event = lambda: blocked(Blocked.EVENT)
        self._add_shortcut('e', event)

    def _add_shortcut(self, hotkey, callback):
        shortcut = QShortcut(self.parent)
        shortcut.setKey(QKeySequence(hotkey))
        shortcut.activated.connect(callback)
