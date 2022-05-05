from typing import Any
from model.Sportsman import Sportsman
from model.datastore import DataStore 
from kivymd.app import MDApp

from view.SearchDialogs import NameAndSportSearchDialogue, NameAndSportSearchResults

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
        #If we don't have any data, why even bother? I'll leave the save of empty files just in case
        #if len(self.getData()) == 0: return
        self.data.save(path)

    def addRecord(self, record: dict[str, Any]):
        try:
            self.data.addRecord(Sportsman(**record))
        except ValueError:
            pass

    def searchByNameOrSportResults(self, name: str, sport: str) -> None:
        data = self.data.searchByNameOrSport(name, sport)
        dialog = NameAndSportSearchResults(data)
        dialog.open()

    def searchByNameOrSportDialogue(self) -> None:
            self.dialog = NameAndSportSearchDialogue()
            self.dialog.open()

    def searchByNameOrRank(self) -> None:
        pass 

    def searchByTitles(self) -> None:
        pass

    def deleteByNameOrSport(self, name: str, sport: str) -> int:
        return self.data.deleteByNameOrSport(name, sport)

    def deleteByNameOrRank(self, name: str, rank: str) -> int:
        return self.data.deleteByNameOrRank(name, rank)

    def deleteByTitles(self, min: int, max: int) -> int:
        return self.data.deleteByTitles(min, max)

    def updateTable(self):
        MDApp.get_running_app().root.updateTable()

    def getData(self):
        return self.data.getData()