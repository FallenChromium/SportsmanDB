import abc
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.menu import MDDropdownMenu
from view.constants import table_fields

from kivymd.app import MDApp

Builder.load_file("ui/SearchDialogs.kv")
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
                MDFlatButton(text="OK",on_press=self.openResults),
            ],
        )

class SearchInput(MDBoxLayout):
    pass

class ResultsTable(MDBoxLayout):
    def __init__(self, data: list):
        super().__init__()
        table = MDDataTable(size_hint=(1, 0.95),
                column_data=[(x, dp(30)) for x in table_fields],
                use_pagination=True,
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
    sport_dropdown = ObjectProperty(None)
    def __init__(self):
        super().__init__()
        self.sport_dropdown = MDDropdownMenu(
            caller=self.ids.sport,
            items=[
            {
                "text": sport,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=sport: self.set_sport(x),
            } for sport in MDApp.get_running_app().controller.getSportsList()
            ],
            position="bottom",
            width_mult=4,
        )

    def set_sport(self, text_item):
        self.ids.sport.text = text_item
        self.sport_dropdown.dismiss()

class NameAndRankInput(SearchInput):
    rank_dropdown = ObjectProperty(None)
    def __init__(self):
        super().__init__()
        self.rank_dropdown = MDDropdownMenu(
            caller=self.ids.rank,
            items=[
            {
                "text": rank,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=rank: self.set_rank(x),
            } for rank in MDApp.get_running_app().controller.getRanksList()
            ],
            position="bottom",
            width_mult=4,
        )

    def set_rank(self, text_item):
        self.ids.rank.text = text_item
        self.rank_dropdown.dismiss()

class TitlesAmountInput(SearchInput):
    pass

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