from PySide6.QtWidgets import QWidget, QDialog, QTabWidget, QVBoxLayout


class Help(QDialog):
    def __init__(self):
        super().__init__()

        self._visible = False

        tab_widget = QTabWidget()
        tab_widget.addTab(HelpTab(self), "Help")
        tab_widget.addTab(HotkeyTab(self), "Hotkey settings")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
        self.setWindowTitle("Help")

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self.setVisible(value)
        self._visible = value


class HelpTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)


class HotkeyTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
