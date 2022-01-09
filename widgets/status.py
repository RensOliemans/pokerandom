from PySide6.QtWidgets import QLabel, QGridLayout, QGroupBox


class Status(QGroupBox):
    def __init__(self, add_link_callback, get_name_of_location):
        super().__init__()

        self._entrance = None
        self.add_link_callback = add_link_callback
        self.get_name_of_location = get_name_of_location

        self.layout = QGridLayout(self)

        self.layout.addWidget(QLabel('Entrance (E)'), 0, 0)
        self.layout.addWidget(QLabel('Destination (D)'), 0, 1)

        self.entrance_widget = QLabel('Select a location')
        self.destination_widget = QLabel('')

        self.layout.addWidget(self.entrance_widget, 1, 0)
        self.layout.addWidget(self.destination_widget, 1, 1)

    def select_item(self, key):
        if self.entrance is None:
            self.entrance = key
        elif self.entrance == key:
            return
        elif key == 'dead_end':
            self.add_link_callback(self.entrance, 'dead_end')
            self.entrance = None
        else:
            self.add_link_callback(self.entrance, key)
            self.entrance = None

    @property
    def entrance(self):
        return self._entrance

    @entrance.setter
    def entrance(self, key):
        self._entrance = key
        if key is None:
            self.entrance_widget.setText('Select a location')
            self.destination_widget.setText('')
        else:
            name = self.get_name_of_location(key)
            self.entrance_widget.setText(name)
            self.destination_widget.setText("Select a location")
