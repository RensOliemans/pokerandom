from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QDialog, QTabWidget, QVBoxLayout, QTextEdit, QLabel

HOTKEY = "Hotkey settings"


class Help(QDialog):
    def __init__(self):
        super().__init__()

        tab_widget = QTabWidget()
        tab_widget.addTab(HelpTab(self), "Help")
        tab_widget.addTab(HotkeyTab(self), HOTKEY)

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
        self.setWindowTitle("Help")


class HelpTab(QLabel):
    def __init__(self, parent):
        super().__init__(parent)

        self.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.setOpenExternalLinks(True)
        self.setTextFormat(Qt.RichText)

        self.setText(f"""
        Click on an entrance and destination to link the two. <br>
        Press 'q' or Esc to cancel the link, see {HOTKEY} for more hotkeys.
        <br>
        Hold Shift while hovering over an entrance to see all desinations available
        <br>
        <i>within 2 warps</i>.
        <br>
        Control-click on an entrance to immediately switch to its destination.
                
        <h3>About</h3>
        A tool to keep track of the random locations in randomized Pokémon.
        <br>
        Credits to the randomization to <a href="https://www.youtube.com/c/PointCrow">PointCrow</a>.
        <br>
        See <a href="https://www.reddit.com/r/pokemon/comments/qel5h4/">here</a> for the Reddit
        post explaining how it works (for Emerald).
        <br>
        This tool is open-source, <a href="https://gitlab.com/RensOliemans/pokerandom">here</a> is the source-code.
        """)


class HotkeyTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
