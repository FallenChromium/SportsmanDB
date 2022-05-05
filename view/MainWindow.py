from kivy.metrics import dp
from kivymd.uix.stacklayout import StackLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from view.ActionPanel import ActionPanel
from view.constants import table_fields


Builder.load_file('ui/ActionPanel.kv')


    

class MainWindow(StackLayout):
    data_tables = ObjectProperty(None)
    action_panel = ObjectProperty(None)
    def __init__(self):
        super().__init__()
        self.data_tables = MDDataTable(
            size_hint=(1, 0.95),
            use_pagination=True,
            column_data=[(x, dp(30)) for x in table_fields],
            row_data=[],
        )
        self.action_panel = ActionPanel(size_hint=(1, 0.1))
        self.add_widget(self.data_tables)
        self.add_widget(self.action_panel)
    
    def updateTable(self):
        data = [(idx, record.name, record.cast, record.position, record.titles, record.sport, record.rank) for idx, record in enumerate(MDApp.get_running_app().controller.getData())]
        self.data_tables.update_row_data(instance_data_table=self.data_tables, data=data)
