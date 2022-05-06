from typing import Any
from model.Sportsman import Sportsman
from model.datastore import DataStore
from kivymd.app import MDApp

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

    def addRecord(self, record: dict[str, Any]):
        try:
            self.data.addRecord(Sportsman(**record))
        except ValueError:
            pass

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


    def deleteByNameOrSport(self, name: str, sport: str) -> int:
        return self.data.deleteByNameOrSport(name, sport)

    def deleteByNameOrRank(self, name: str, rank: str) -> int:
        return self.data.deleteByNameOrRank(name, rank)

    def deleteByTitles(self, min: int, max: int) -> int:
        return self.data.deleteByTitles(min, max)

    def getSportsList(self) -> list[str]:
        return self.data.sportsList()

    def getRanksList(self) -> list[str]:
        return self.data.ranksList()

    def updateTable(self):
        MDApp.get_running_app().root.updateTable()

    def getData(self):
        return self.data.getData()
