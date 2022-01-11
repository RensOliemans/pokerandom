from PySide6.QtGui import QShortcut, QKeySequence

from util.blocked import Blocked


class Shortcuts:
    def __init__(self, parent, cancel, one_way, blocked):
        self.parent = parent

        dead_end = lambda: blocked(Blocked.DEAD_END)
        cut = lambda: blocked(Blocked.CUT)
        rock_smash = lambda: blocked(Blocked.ROCK_SMASH)
        strength = lambda: blocked(Blocked.STRENGTH)
        surf = lambda: blocked(Blocked.SURF)
        waterfall = lambda: blocked(Blocked.WATERFALL)
        rock_climb = lambda: blocked(Blocked.ROCK_CLIMB)
        trainer = lambda: blocked(Blocked.TRAINER)
        event = lambda: blocked(Blocked.EVENT)

        self._add_shortcut('q', cancel)
        self._add_shortcut('1', one_way)
        self._add_shortcut('d', dead_end)
        self._add_shortcut('c', cut)
        self._add_shortcut('r', rock_smash)
        self._add_shortcut('s', strength)
        self._add_shortcut('f', surf)
        self._add_shortcut('w', waterfall)
        self._add_shortcut('b', rock_climb)
        self._add_shortcut('t', trainer)
        self._add_shortcut('e', event)

    def _add_shortcut(self, hotkey, callback):
        shortcut = QShortcut(self.parent)
        shortcut.setKey(QKeySequence(hotkey))
        shortcut.activated.connect(callback)
