from os import O_NONBLOCK
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.stacklayout import StackLayout
from kivy.properties import ObjectProperty
from plyer import filechooser

from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable

from controller.AppController import AppController

controller = AppController()

Builder.load_file('ui/ActionPanel.kv')

class ActionPanel(StackLayout):
    def open(self, filename):
        controller.openFile(filename)

    def openDialog(self):
        # Kivy file dialog sucks a ton - I want to open a native one instead :)
        path = filechooser.open_file(title="Open an xml file containing the DB", filters=[("*.xml")])
        # check if the user actually chose anything
        if path is not None:
            # because filechooser returns a list of chosen paths. We do not support multi-file import yet
            self.open(path[0])
        else: 
            pass
    
    def save(self):
            path = filechooser.save_file(title="Enter a filename for the dump file", filters=[("*.xml")]) 
            controller.saveFile(path[0])
    

class MainWindow(StackLayout):
    data_tables = ObjectProperty(None)
    action_panel = ObjectProperty(None)
    def __init__(self):
        super().__init__()
        self.data_tables = MDDataTable(
            size_hint=(1, 0.95),
            use_pagination=True,
            column_data=[
                ("No.", dp(30)),
                ("Имя", dp(30)),
                ("cast", dp(30)),
                ("Позиция", dp(30)),
                ("Титулов", dp(30)),
                ("Вид спорта", dp(30)),
                ("Разряд", dp(30)),
            ],
            row_data=[
            ],
        )
        self.action_panel = ActionPanel(size_hint=(1, 0.1))
        self.add_widget(self.data_tables)
        self.add_widget(self.action_panel)
    
    def updateTable(self):
        data = [(idx, record.name, record.cast, record.position, record.titles, record.sport, record.rank) for idx, record in enumerate(controller.getData())]
        self.data_tables.update_row_data(instance=self.data_tables, value=data)
