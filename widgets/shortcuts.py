from PySide6.QtGui import QShortcut, QKeySequence


class Shortcuts:
    def __init__(self, parent, cancel, one_way, dead_end):  #, deadend, cut, rocksmash, strength, surf, rockclimb, waterfall, trainer, event):
        self.parent = parent

        self._add_shortcut('q', cancel)
        self._add_shortcut('1', one_way)
        self._add_shortcut('d', dead_end)
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
