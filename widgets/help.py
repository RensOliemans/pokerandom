from PySide6.QtWidgets import QWidget, QDialog, QTabWidget, QVBoxLayout


class Help(QDialog):
    def __init__(self):
        super().__init__()

        tab_widget = QTabWidget()
        tab_widget.addTab(HelpTab(self), "Help")
        tab_widget.addTab(HotkeyTab(self), "Hotkey settings")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
        self.setWindowTitle("Help")


class HelpTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)


class HotkeyTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
