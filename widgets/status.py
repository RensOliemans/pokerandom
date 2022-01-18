from PySide6.QtWidgets import QLabel, QGroupBox, QGridLayout, QVBoxLayout, QTextEdit

from widgets import Note


class Status:
    def __init__(self, selected_callback, add_link_callback, get_name_of_location):

        self._entrance = None
        self._one_way = False
        self.selected_callback = selected_callback
        self.add_link_callback = add_link_callback
        self.get_name_of_location = get_name_of_location

        self.note = Note(self.save_note)
        self.widget = StatusWidget(self.note)

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
        self.widget.change_oneway(value)

    @property
    def entrance(self):
        return self._entrance

    @entrance.setter
    def entrance(self, value):
        self._entrance = value
        self.widget.change_entrance(value)
        self.selected_callback(value, selected=value is not None)


class StatusWidget(QGroupBox):
    def __init__(self, note):
        super().__init__('Current Edit')

        self.entrance_widget = QLabel()
        self.one_way_widget = QLabel()

        self.change_entrance()

        self.layout = QGridLayout(self)

        self.layout.addWidget(self.entrance_widget, 0, 0)
        self.layout.addWidget(self.one_way_widget, 1, 0)
        self.layout.addWidget(note, 0, 1)

    def change_entrance(self, value=None):
        text = f"Selected '{value.name}'" if value else 'Select a location'
        self.entrance_widget.setText(text)

    def change_oneway(self, text=None):
        text = f'One-way enabled' if text else ''
        self.one_way_widget.setText(text)
