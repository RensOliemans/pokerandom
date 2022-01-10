from PySide6.QtCore import QSize
from PySide6.QtWidgets import QLabel, QGroupBox, QGridLayout


class Status(QGroupBox):
    def __init__(self, add_link_callback, get_name_of_location):
        super().__init__('Current Edit')

        self._entrance = None
        self.add_link_callback = add_link_callback
        self.get_name_of_location = get_name_of_location

        self.entrance_widget = QLabel('Select a location')
        self.destination_widget = QLabel('')

        self.layout = QGridLayout(self)

        self.layout.addWidget(self.entrance_widget, 1, 0)
        self.layout.addWidget(self.destination_widget, 1, 1)

    def select_item(self, key):
        if self.entrance is None:
            self.entrance = key
        elif self.entrance == key:
            return
        else:
            self.add_link_callback(self.entrance, key)
            self.entrance = None

    def cancel(self):
        self.entrance = None

    @property
    def entrance(self):
        return self._entrance

    @entrance.setter
    def entrance(self, value):
        self._entrance = value
        if value is None:
            self.entrance_widget.setText('Select a location')
        else:
            self.entrance_widget.setText(f"Selected '{self.get_name_of_location(value)}'")
