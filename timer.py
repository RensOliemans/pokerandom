from PySide6.QtCore import QTimer
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication


def connect_shift(qapp: QApplication, poke, down, up):
    timer = QTimer(qapp)
    timer.timeout.connect(lambda: check_for_shift(qapp, down, up))
    timer.start(100)


def check_for_shift(qapp, down, up):
    modifiers = qapp.queryKeyboardModifiers()
    if modifiers == Qt.ShiftModifier:
        down()
    else:
        up()
