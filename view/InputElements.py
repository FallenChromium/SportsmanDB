from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("ui/InputElements.kv")

class SearchInput(MDBoxLayout):
    pass

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