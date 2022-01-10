from PySide6.QtGui import QShortcut, QKeySequence


class Shortcuts:
    def __init__(self, parent, cancel, oneway):  #, deadend, cut, rocksmash, strength, surf, rockclimb, waterfall, trainer, event):
        self.parent = parent

        self.add_cancel(cancel)
        self.add_oneway(oneway)
        # self.add_deadend()
        # self.add_cut()
        # self.add_rocksmash()
        # self.add_strength()
        # self.add_surf()
        # self.add_rockclimb()
        # self.add_waterfall()
        # self.add_trainer()
        # self.add_event()

    def add_cancel(self, callback):
        cancel = QShortcut(self.parent)
        cancel.setKey(QKeySequence('c'))
        cancel.activated.connect(callback)

    def add_oneway(self, callback):
        oneway = QShortcut(self.parent)
        oneway.setKey(QKeySequence('1'))
        oneway.activated.connect(callback)
