
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu

class InsertErrorDialog(MDDialog):
    def __init__(self): 
        super().__init__(
                text="Incorrect data input. Please try again",
                title= "Error",
                buttons=[
                    MDFlatButton(
                        text="CLOSE",
                        theme_text_color="Custom",
                        on_press=self.dismiss
                    ),
                ],)

class InsertInput(MDBoxLayout):
    def set_rank(self, text_item):
        self.ids.rank.text = text_item
        self.rank_dropdown.dismiss()

    def set_sport(self, text_item):
        self.ids.sport.text = text_item
        self.sport_dropdown.dismiss()

    def set_cast(self, text_item):
        self.ids.cast.text = text_item
        self.cast_dropdown.dismiss()

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
        self.cast_dropdown = MDDropdownMenu(
            caller=self.ids.cast,
            items=[
            {
                "text": cast,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=cast: self.set_cast(x),
            } for cast in MDApp.get_running_app().controller.getCastsList()
            ],
            position="bottom",
            width_mult=4,
        )  
    

Builder.load_file('ui/InsertDialog.kv')

class InsertDialog(MDDialog):

    def insertRecord(self, *args):
        name = self.content_cls.ids.fullname.text
        cast = self.content_cls.ids.cast.text
        position = self.content_cls.ids.position.text
        titles = self.content_cls.ids.titles.text
        sport = self.content_cls.ids.sport.text
        rank = self.content_cls.ids.rank.text

        MDApp.get_running_app().controller.addRecordResults({"name": name, "cast": cast, "position": position, "titles": titles, "sport": sport, "rank": rank})

    def __init__(self):
        super().__init__(
            title="Insert record:",
            type="custom",            
            content_cls=InsertInput(),
            buttons=[
                MDFlatButton(text="CANCEL", on_press=self.dismiss),
                MDFlatButton(text="INSERT",on_press=self.insertRecord),
            ],
        )