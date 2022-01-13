import sys
import logging
from os.path import join

from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import QApplication

from data.platinum import CATEGORIES, INITIAL_LOCATION
from pokerandom import PokeRandom
from links.db import Db
from timer import connect_shift

logging.basicConfig(filename=join('data', 'pokerandom.log'), level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')
database = join('data', 'links.sqlite')


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication()
    with Db(database) as db:
        pokerandom = PokeRandom(categories=CATEGORIES, initial_location=INITIAL_LOCATION, db=db)
        timer = connect_shift(app,
                              pokerandom.connections.show_double_connections,
                              pokerandom.connections.hide_double_connections)
        pokerandom.show()
        sys.exit(app.exec())
