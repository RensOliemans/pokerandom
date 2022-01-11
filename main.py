import sys
import logging
from os.path import join

from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import QApplication

from data.platinum import LOCATIONS, ENTRANCES
from pokerandom import PokeRandom
from links.db import Db

logging.basicConfig(filename=join('data', 'pokerandom.log'), level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')
database = join('data', 'links.sqlite')


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication()
    with Db(database) as db:
        print(app.queryKeyboardModifiers())
        pokerandom = PokeRandom(locations=LOCATIONS, initial_location=LOCATIONS['cities'][0],
                                entrances=ENTRANCES, db=db)
        pokerandom.show()
        sys.exit(app.exec())
