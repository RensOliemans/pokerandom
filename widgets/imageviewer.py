from os.path import join

from PySide6.QtCore import QDir
from PySide6.QtGui import QImageReader, QGuiApplication, QPixmap
from PySide6.QtWidgets import QLabel, QMessageBox


class ImageViewer(QLabel):
    def __init__(self, initial_city, max_width=1000):
        super().__init__()

        self.max_width = max_width
        self.set_image(initial_city)

    def set_image(self, cityname):
        filename = self._convert_city_to_imagename(cityname)
        image = self._load_image(filename)
        if image:
            pixmap = QPixmap.fromImage(image)
            pixmap = pixmap.scaledToWidth(self.max_width)
            self.setPixmap(pixmap)

    def _load_image(self, filename):
        native_filename = QDir.toNativeSeparators(filename)

        reader = QImageReader(filename)
        reader.setAutoTransform(True)
        new_image = reader.read()
        if new_image.isNull():
            error = reader.errorString()
            QMessageBox.information(self, QGuiApplication.applicationDisplayName(),
                                    f"Cannot load {native_filename}: {error}")
            return False

        return new_image

    @staticmethod
    def _convert_city_to_imagename(current_city):
        return join('images', f'{current_city}.png')
