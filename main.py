from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable


class Example(MDApp):
    def build(self):
        layout = AnchorLayout()
        data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("No.", dp(30)),
                ("name", dp(30)),
                ("cast", dp(30)),
                ("position", dp(30)),
                ("title", dp(30)),
                ("sport", dp(30)),
                ("rank", dp(30)),
            ],
            row_data=[
                (idx, record.name, record.cast, record.position, record.title, record.sport, record.rank) for idx, record in enumerate(records)
            ],
        )
        layout.add_widget(data_tables)
        return layout


Example().run()