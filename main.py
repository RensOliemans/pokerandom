import sys
import logging

from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import QApplication

from platinum import LOCATIONS, ENTRANCES
from pokerandom import PokeRandom

logging.basicConfig(filename='pokerandom.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication()
    gallery = PokeRandom(locations=LOCATIONS, initial_location=LOCATIONS['cities'][1], entrances=ENTRANCES)
    gallery.show()
    sys.exit(app.exec())
