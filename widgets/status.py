from PySide6.QtWidgets import QLabel, QGroupBox, QGridLayout, QVBoxLayout, QTextEdit

from widgets import Note


class Status(QGroupBox):
    def __init__(self, selected_callback, add_link_callback, get_name_of_location):
        super().__init__('Current Edit')

        self._entrance = None
        self._one_way = False
        self.selected_callback = selected_callback
        self.add_link_callback = add_link_callback
        self.get_name_of_location = get_name_of_location

        self.entrance_widget = QLabel('Select a location')
        self.note = Note(self, self.save_note)
        self.one_way_widget = QLabel('')

        self.layout = QGridLayout(self)

        self.layout.addWidget(self.entrance_widget, 0, 0)
        self.layout.addWidget(self.one_way_widget, 1, 0)
        self.layout.addWidget(self.note, 0, 1)

    def select_item(self, entrance):
        if self.entrance is None:
            self.entrance = entrance
        elif self.entrance == entrance:
            return
        else:
            self.save(destination=entrance, one_way=self.one_way)

    def cancel(self):
        self.entrance = None
        self.one_way = False
        self.note.clearFocus()

    def oneway(self):
        self.one_way = not self.one_way

    def blocked(self, block):
        if self.entrance is None:
            return
        else:
            self.save(block=block)

    def show_note(self):
        self.note.setFocus()

    def save_note(self, note):
        if self.entrance is None:
            return

        self.save(note=note)
        self.note.clear()

    def save(self, *, destination=None, one_way=False, block=None, note=None):
        destination = destination.key if destination else None
        self.add_link_callback(self.entrance.key, destination, one_way=one_way, block=block, note=note)
        self.cancel()

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
            self.entrance_widget.setText(f"Selected '{value.name}'")
        self.selected_callback(value, selected=value is not None)
