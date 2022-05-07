from typing import Any
from model.Sportsman import Sportsman
from model.datastore import DataStore
from model.constants import IncorrectFileException
from kivymd.app import MDApp
from view.DeleteDialogs import NameAndRankDeleteDialogue, NameAndSportDeleteDialogue, TitlesAmountDeleteDialogue, DeletionReportDialog
from view.InsertDialog import InsertDialog, InsertErrorDialog

from view.SearchDialogs import NameAndRankSearchDialogue, NameAndSportSearchDialogue, ResultsDialog, TitlesAmountSearchDialogue


class AppController:
    def __init__(self):
        self.data = DataStore()
        self.filename = ""
        self.dialog = None

    # Action Panel functions
    def openFile(self, filename: str):
        self.filename = filename
        self.data.load(self.filename)
        self.updateTable()

    def saveFile(self, path: str):
        # If we don't have any data, why even bother? I'll leave the save of empty files just in case
        # if len(self.getData()) == 0: return
        self.data.save(path)

    def addRecordResults(self, record: dict[str, Any]):
        try:
            object = Sportsman(**record)
            index = self.data.addRecord(object)
            MDApp.get_running_app().root.addRow(index, object)
            self.dialog.dismiss()
        except IncorrectFileException:
            InsertErrorDialog().open()


    def addRecord(self):
        self.dialog = InsertDialog()
        self.dialog.open() 

    def searchByNameOrSportResults(self, name: str, sport: str) -> None:
        self.dialog.dismiss()
        data = self.data.searchByNameOrSport(name, sport)
        ResultsDialog(data).open()

    def searchByNameOrRankResults(self, name: str, rank: str) -> None:
        self.dialog.dismiss()
        data = self.data.searchByNameOrRank(name, rank)
        ResultsDialog(data).open()

    def searchByTitlesResults(self, min: int, max: int) -> None:
        self.dialog.dismiss()
        data = self.data.searchByTitles(min, max)
        ResultsDialog(data).open()


    def searchByNameOrSport(self) -> None:
        self.dialog = NameAndSportSearchDialogue()
        self.dialog.open()

    def searchByNameOrRank(self) -> None:
        self.dialog = NameAndRankSearchDialogue()
        self.dialog.open()

    def searchByTitles(self) -> None:
        self.dialog = TitlesAmountSearchDialogue()
        self.dialog.open()

    def deleteByNameOrSport(self) -> None:
        self.dialog = NameAndSportDeleteDialogue()
        self.dialog.open()

    def deleteByNameOrRank(self) -> None:
        self.dialog = NameAndRankDeleteDialogue()
        self.dialog.open()

    def deleteByTitles(self) -> None:
        self.dialog = TitlesAmountDeleteDialogue()
        self.dialog.open()

    def deleteByNameOrSportResults(self, name: str, sport: str) -> None:
        self.dialog.dismiss()
        DeletionReportDialog(self.data.deleteByNameOrSport(name, sport)).open()
        self.updateTable()

    def deleteByNameOrRankResults(self, name: str, rank: str) -> None:
        self.dialog.dismiss()
        DeletionReportDialog(self.data.deleteByNameOrRank(name, rank)).open()
        self.updateTable()

    def deleteByTitlesResults(self, min: int, max: int) -> None:
        self.dialog.dismiss()
        DeletionReportDialog(self.data.deleteByTitles(min, max)).open()
        self.updateTable()

    def getSportsList(self) -> list[str]:
        return self.data.sportsList()

    def getRanksList(self) -> list[str]:
        return self.data.ranksList()

    def getCastsList(self) -> list[str]:
        return self.data.castsList()

    def updateTable(self):
        MDApp.get_running_app().root.updateTable()

    def getData(self):
        return self.data.getData()
