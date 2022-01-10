from PySide6.QtWidgets import QWidget


class Widget:
    def __init__(self, key, widget: QWidget):
        self.key = key
        self.widget: QWidget = widget

    def __eq__(self, other):
        return (isinstance(other, Widget) and self.key == other.key
                or self.key == other)

    def __hash__(self):
        return hash(self.key)
