import logging
from os.path import join

from PySide6.QtCore import QDir, Qt
from PySide6.QtGui import QImageReader, QPixmap
from PySide6.QtWidgets import QLabel

from errors import ImageNotFoundError


class ImageViewer(QLabel):
    def __init__(self, max_width=1000, max_height=1000):
        super().__init__()

        self.max_width = max_width
        self.max_height = max_height

    def set_image(self, location):
        filename = self._convert_city_to_imagename(location)
        try:
            image = self._load_image(filename)
        except ImageNotFoundError as e:
            logging.info(e)
            return

        if image:
            pixmap = QPixmap.fromImage(image)
            pixmap = pixmap.scaled(self.max_width, self.max_height, Qt.AspectRatioMode.KeepAspectRatio)
            self.setPixmap(pixmap)

    @staticmethod
    def _load_image(filename):
        native_filename = QDir.toNativeSeparators(filename)

        reader = QImageReader(filename)
        reader.setAutoTransform(True)
        new_image = reader.read()
        if new_image.isNull():
            raise ImageNotFoundError(f'Could not load image: {native_filename}. Error: {reader.errorString()}')

        return new_image

    @staticmethod
    def _convert_city_to_imagename(current_city):
        return join('images', f'{current_city}.png')
