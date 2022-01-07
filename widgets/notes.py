from PySide6.QtWidgets import QToolBox, QPlainTextEdit


class Notes(QToolBox):
    def __init__(self):
        super().__init__()

        plain_textedit = QPlainTextEdit("")
        self.addItem(plain_textedit, "Notes")
