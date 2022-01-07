import sys

from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import QApplication
from pokerandom import PokeRandom

from cities import PLATINUM


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication()
    gallery = PokeRandom(cities=PLATINUM, initial_city=PLATINUM[0][0])
    gallery.show()
    sys.exit(app.exec())