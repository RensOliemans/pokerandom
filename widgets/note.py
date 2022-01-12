from PySide6.QtWidgets import QTextEdit, QLineEdit

from util import hotkeys


class Note(QLineEdit):
    def __init__(self, parent, callback):
        super().__init__(parent)

        self.callback = callback
        self.setPlaceholderText(f'Select a location, hit {hotkeys.MAP_NOTE[0]} and type+enter to map to a note.')
        self.returnPressed.connect(self.finished)

    def finished(self):
        self.callback(self.text())
