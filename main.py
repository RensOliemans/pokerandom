import sys

from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import QApplication
from pokerandom import PokeRandom

from platinum import LOCATIONS, ENTRANCES


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication()
    gallery = PokeRandom(locations=LOCATIONS, initial_location=LOCATIONS['cities'][1], entrances=ENTRANCES)
    gallery.show()
    sys.exit(app.exec())
