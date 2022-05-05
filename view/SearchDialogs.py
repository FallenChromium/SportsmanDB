from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from view.constants import table_fields
from kivymd.app import MDApp


class SearchDialog(MDDialog):
    def __init__(self, content):
        super().__init__(
            title="Search:",
            type="custom",            
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_press=self.dismiss
                ),
                MDFlatButton(
                    text="OK",
                    on_press=self.openResults,
                ),
            ],
        )

class SearchInput(MDBoxLayout):
    pass

class ResultsTable(MDBoxLayout):
    def __init__(self, data: list):
        super().__init__()
        table = MDDataTable(size_hint=(1, 0.95),
                column_data=[(x, dp(30)) for x in table_fields],
                row_data=[(idx, record.name, record.cast, record.position, record.titles, record.sport, record.rank) for idx, record in enumerate(data)])
        self.add_widget(table)


class ResultsDialog(MDDialog):
    def __init__(self, data: list):
        content = ResultsTable(data)
        super().__init__(
                size_hint= [0.9, None],
                title="Search results:",
                type="custom",
                content_cls = content,
                buttons=[
                    MDFlatButton(
                        text="CLOSE",
                        theme_text_color="Custom",
                        on_press=self.dismiss
                    ),
                ],
        )


class NameAndSportInput(SearchInput):
    pass

class NameAndRankInput(SearchInput):
    pass

class TitlesInput(SearchInput):
    pass


class NameAndSportSearchResults(ResultsDialog):
    def __init__(self, table_data: list):
        super().__init__(table_data)

class NameAndSportSearchDialogue(SearchDialog):
    def openResults(self, *args):
        fullname = self.content_cls.ids.fullname.text
        sport = self.content_cls.ids.sport.text
        MDApp.get_running_app().controller.searchByNameOrSportResults(fullname,sport)

    def __init__(self):
        super().__init__(NameAndSportInput())
        
        
    
Builder.load_file("ui/SearchDialogs.kv")
Builder.load_file("ui/ResultsDialogs.kv")