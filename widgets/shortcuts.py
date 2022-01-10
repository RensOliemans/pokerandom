from PySide6.QtGui import QShortcut, QKeySequence

from util.blocked import Blocked


class Shortcuts:
    def __init__(self, parent, cancel, one_way, blocked):
        self.parent = parent

        dead_end = lambda: blocked(Blocked.DEAD_END)
        cut = lambda: blocked(Blocked.CUT)

        self._add_shortcut('q', cancel)
        self._add_shortcut('1', one_way)
        self._add_shortcut('d', dead_end)
        self._add_shortcut('c', cut)
        # self.add_cut()
        # self.add_rocksmash()
        # self.add_strength()
        # self.add_surf()
        # self.add_rockclimb()
        # self.add_waterfall()
        # self.add_trainer()
        # self.add_event()

    def _add_shortcut(self, hotkey, callback):
        shortcut = QShortcut(self.parent)
        shortcut.setKey(QKeySequence(hotkey))
        shortcut.activated.connect(callback)
