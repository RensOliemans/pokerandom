from PySide6.QtWidgets import QLabel, QGroupBox, QGridLayout


class Status(QGroupBox):
    def __init__(self, add_link_callback, get_name_of_location):
        super().__init__('Current Edit')

        self._entrance = None
        self._one_way = False
        self.add_link_callback = add_link_callback
        self.get_name_of_location = get_name_of_location

        self.entrance_widget = QLabel('Select a location')
        self.destination_widget = QLabel('')
        self.one_way_widget = QLabel('')

        self.layout = QGridLayout(self)

        self.layout.addWidget(self.entrance_widget, 0, 0)
        self.layout.addWidget(self.one_way_widget, 1, 1)
        self.layout.addWidget(self.destination_widget, 0, 1)

    def select_item(self, key):
        if self.entrance is None:
            self.entrance = key
        elif self.entrance == key:
            return
        else:
            self.add_link_callback(self.entrance, key, self._one_way)
            self.entrance = None
            self.one_way = False

    def cancel(self):
        self.entrance = None

    def oneway(self):
        self.one_way = not self.one_way

    def blocked(self, block):
        if self.entrance is None:
            return
        else:
            print(block)
            self.add_link_callback(self.entrance, destination=None, one_way=False, block=block)
            self.entrance = None

    @property
    def one_way(self):
        return self._one_way

    @one_way.setter
    def one_way(self, value):
        self._one_way = value
        if value:
            self.one_way_widget.setText('One-way enabled')
        else:
            self.one_way_widget.setText('')

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
