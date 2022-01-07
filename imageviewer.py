from PySide6.QtCore import QDir
from PySide6.QtGui import QImageReader, QGuiApplication, QPixmap
from PySide6.QtWidgets import QLabel, QMessageBox


class ImageViewer(QLabel):
    def __init__(self, initial_city):
        super().__init__()

        self.set_image(initial_city)

    def set_image(self, cityname):
        filename = self._convert_city_to_imagename(cityname)
        image = self._load_image(filename)
        if image:
            self.setPixmap(QPixmap.fromImage(image))

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
        return f'images/{current_city}.png'
