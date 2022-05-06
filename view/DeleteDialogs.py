import abc
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from view.InputElements import NameAndSportInput, NameAndRankInput, TitlesAmountInput

from kivymd.app import MDApp

Builder.load_file("ui/ResultsDialogs.kv")


class DeleteDialog(MDDialog):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def deleteRecords(self, *args):
        pass

    def __init__(self, content):
        super().__init__(
            title="Delete records:",
            type="custom",            
            content_cls=content,
            buttons=[
                MDFlatButton(text="CANCEL", on_press=self.dismiss),
                MDFlatButton(text="DELETE",on_press=self.deleteRecords),
            ],
        )


class DeletionReportDialog(MDDialog):
    def __init__(self, data: int):
        super().__init__(
                size_hint= [0.9, None],
                title="Deletion results:",
                text= "No records were deleted" if data == 0 else str(data) + " records were deleted",
                buttons=[
                    MDFlatButton(
                        text="CLOSE",
                        theme_text_color="Custom",
                        on_press=self.dismiss
                    ),
                ],
        )


class NameAndSportDeleteDialogue(DeleteDialog):
    def deleteRecords(self, *args):
        fullname = self.content_cls.ids.fullname.text
        sport = self.content_cls.ids.sport.text
        MDApp.get_running_app().controller.deleteByNameOrSportResults(fullname,sport)

    def __init__(self):
        super().__init__(NameAndSportInput())

class NameAndRankDeleteDialogue(DeleteDialog):
    def deleteRecords(self, *args):
        fullname = self.content_cls.ids.fullname.text
        rank = self.content_cls.ids.rank.text
        MDApp.get_running_app().controller.deleteByNameOrRankResults(fullname,rank)

    def __init__(self):
        super().__init__(NameAndRankInput())
        
class TitlesAmountDeleteDialogue(DeleteDialog):
    def deleteRecords(self, *args):
        min = int(self.content_cls.ids.min_titles.text)
        max = int(self.content_cls.ids.max_titles.text)
        MDApp.get_running_app().controller.deleteByTitlesResults(min,max)

    def __init__(self):
        super().__init__(TitlesAmountInput()) 