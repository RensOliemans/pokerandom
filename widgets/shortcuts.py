from PySide6.QtGui import QShortcut, QKeySequence

from util import hotkeys
from util.blocked import Blocked


class Shortcuts:
    def __init__(self, parent, cancel, one_way, show_note, blocked, show_help):
        self.parent = parent

        self._add_shortcuts(hotkeys.HELP, show_help)

        dead_end = lambda: blocked(Blocked.DEAD_END)
        cut = lambda: blocked(Blocked.CUT)
        rock_smash = lambda: blocked(Blocked.ROCK_SMASH)
        strength = lambda: blocked(Blocked.STRENGTH)
        surf = lambda: blocked(Blocked.SURF)
        waterfall = lambda: blocked(Blocked.WATERFALL)
        rock_climb = lambda: blocked(Blocked.ROCK_CLIMB)
        trainer = lambda: blocked(Blocked.TRAINER)
        event = lambda: blocked(Blocked.EVENT)

        self._add_shortcuts(hotkeys.CANCEL, cancel)
        self._add_shortcuts(hotkeys.ONE_WAY, one_way)
        self._add_shortcuts(hotkeys.MAP_NOTE, show_note)

        # Blocks
        self._add_shortcuts(hotkeys.DEAD_END, dead_end)
        self._add_shortcuts(hotkeys.CUT, cut)
        self._add_shortcuts(hotkeys.ROCK_SMASH, rock_smash)
        self._add_shortcuts(hotkeys.STRENGTH, strength)
        self._add_shortcuts(hotkeys.SURF, surf)
        self._add_shortcuts(hotkeys.WATERFALL, waterfall)
        self._add_shortcuts(hotkeys.ROCK_CLIMB, rock_climb)
        self._add_shortcuts(hotkeys.TRAINER, trainer)
        self._add_shortcuts(hotkeys.EVENT, event)

    def _add_shortcuts(self, keys, callback):
        for hotkey in keys:
            shortcut = QShortcut(self.parent)
            shortcut.setKey(QKeySequence(hotkey))
            shortcut.activated.connect(callback)
