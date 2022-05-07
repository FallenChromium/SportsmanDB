import abc
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable

from view.constants import table_fields
from view.InputElements import NameAndSportInput, NameAndRankInput, TitlesAmountInput

from kivymd.app import MDApp

Builder.load_file("ui/ResultsDialogs.kv")
class SearchDialog(MDDialog):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def openResults(self, *args):
        pass

    def __init__(self, content):
        super().__init__(
            title="Search:",
            type="custom",            
            content_cls=content,
            buttons=[
                MDFlatButton(text="CANCEL", on_press=self.dismiss),
                MDFlatButton(text="SEARCH",on_press=self.openResults),
            ],
        )


class ResultsTable(MDBoxLayout):
    def __init__(self, data: list):
        super().__init__()
        table = MDDataTable(size_hint=(1, 0.95),
                column_data=[(x, dp(30)) for x in table_fields],
                use_pagination=True,
                row_data=[(idx, record.name, record.cast, record.position, record.titles, record.sport, record.rank) for idx, record in enumerate(data, start=1)])
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

class NameAndSportSearchDialogue(SearchDialog):
    def openResults(self, *args):
        fullname = self.content_cls.ids.fullname.text
        sport = self.content_cls.ids.sport.text
        MDApp.get_running_app().controller.searchByNameOrSportResults(fullname,sport)

    def __init__(self):
        super().__init__(NameAndSportInput())

class NameAndRankSearchDialogue(SearchDialog):
    def openResults(self, *args):
        fullname = self.content_cls.ids.fullname.text
        rank = self.content_cls.ids.rank.text
        MDApp.get_running_app().controller.searchByNameOrRankResults(fullname,rank)

    def __init__(self):
        super().__init__(NameAndRankInput())
        
class TitlesAmountSearchDialogue(SearchDialog):
    def openResults(self, *args):
        min = int(self.content_cls.ids.min_titles.text)
        max = int(self.content_cls.ids.max_titles.text)
        MDApp.get_running_app().controller.searchByTitlesResults(min,max)

    def __init__(self):
        super().__init__(TitlesAmountInput()) 