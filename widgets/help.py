from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QWidget, QDialog, QTabWidget, QVBoxLayout, QTextEdit, QLabel

from util import hotkeys

HOTKEY = "Hotkey settings"
HELP_TEXT = f"""
Click on an entrance and destination to link the two. <br>
Press 'q' or Esc to cancel the link, see {HOTKEY} for more hotkeys.
<br>
Hold Shift while hovering over an entrance to see all desinations available
<br>
<i>within 2 warps</i>.
<br>
Control-click on an entrance to immediately switch to its destination.
        
<h3>About</h3>
This is a tool to keep track of the random locations in randomized Pokémon.
<br>
Credits for the randomization to <a href="https://www.youtube.com/c/PointCrow">PointCrow</a>.
<br>
See <a href="https://www.reddit.com/r/pokemon/comments/qel5h4/">here</a> for the Reddit
post explaining how it works (for Emerald).
<br>
Images come from Bulbapedia, location compilation comes from
<a href="https://www.reddit.com/r/pokemon/comments/qel5h4/comment/hhupues/?utm_source=share&utm_medium=web2x&context=3">twiddlebit</a>.
<br>
This tool is open-source, <a href="https://gitlab.com/RensOliemans/pokerandom">here</a> is the source-code.
"""


def convert_hotkey(hotkey):
    if hotkey == QKeySequence.HelpContents:
        return '<b>F1 (Windows)/Ctrl+? (macOS)</b>'
    elif hotkey == QKeySequence.Cancel:
        return '<b>Escape (Windows)/Ctrl+. (macOS)</b>'
    else:
        return f'<b>{hotkey}</b>'


HOTKEY_TEXT = f"""
'{" or ".join(convert_hotkey(x) for x in hotkeys.HELP) }' to show this help menu. <br>
'{" or ".join(convert_hotkey(x) for x in hotkeys.CANCEL) }' to cancel the current input. <br>
'{" or ".join(convert_hotkey(x) for x in hotkeys.ONE_WAY) }' to select route as one-way. <br>
'{" or ".join(convert_hotkey(x) for x in hotkeys.DEAD_END) }' to select as dead-end. <br>
'{" or ".join(convert_hotkey(x) for x in hotkeys.CUT) }' to select destination as Cut-blocked. <br>
'{" or ".join(convert_hotkey(x) for x in hotkeys.ROCK_SMASH) }' to select destination as Rock Smash-blocked.<br>
'{" or ".join(convert_hotkey(x) for x in hotkeys.STRENGTH) }' to select destination as Strength-blocked. <br>
'{" or ".join(convert_hotkey(x) for x in hotkeys.SURF) }' to select destination as Surf-blocked. <br>
'{" or ".join(convert_hotkey(x) for x in hotkeys.WATERFALL) }' to select destination as Waterfall-blocked. <br>
'{" or ".join(convert_hotkey(x) for x in hotkeys.ROCK_CLIMB) }' to select destination as Rock Climb-blocked. <br>
'{" or ".join(convert_hotkey(x) for x in hotkeys.TRAINER) }' to select destination as Trainer-blocked. <br>
'{" or ".join(convert_hotkey(x) for x in hotkeys.EVENT) }' to select destination as Event-blocked. <br>
"""


class Help(QDialog):
    def __init__(self):
        super().__init__()

        tab_widget = QTabWidget()
        tab_widget.addTab(Label(self, HELP_TEXT), "Help")
        tab_widget.addTab(Label(self, HOTKEY_TEXT), HOTKEY)

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
        self.setWindowTitle("Help")


class Label(QLabel):
    def __init__(self, parent, text):
        super().__init__(parent)

        self.setTextFormat(Qt.RichText)
        self.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.setOpenExternalLinks(True)

        self.setText(text)


class SmallHelp(QLabel):
    def __init__(self, parent):
        super().__init__(parent)

        self.setText(f'Press {" or ".join(convert_hotkey(x) for x in hotkeys.HELP) } to see help+shortcuts.')
