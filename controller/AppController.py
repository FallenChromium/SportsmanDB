from typing import Any
from model.Sportsman import Sportsman
from model.db import DB 
from kivy.app import App

class AppController:
    def __init__(self):
        self.data = DB()
        self.filename = ""

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

    def updateTable(self):
        app = App.get_running_app()
        app.root.updateTable()

    def searchByNameOrSport(self, name: str, sport: str) -> list:
        return self.data.searchByNameOrSport(name, sport)

    def searchByNameOrRank(self, name: str, rank: str) -> list:
        return self.data.searchByNameOrRank(name, rank)

    def searchByTitles(self, min: int, max: int) -> list:
        return self.data.searchByTitles(min, max)

    def deleteByNameOrSport(self, name: str, sport: str) -> int:
        return self.data.deleteByNameOrSport(name, sport)

    def deleteByNameOrRank(self, name: str, rank: str) -> int:
        return self.data.deleteByNameOrRank(name, rank)

    def deleteByTitles(self, min: int, max: int) -> int:
        return self.data.deleteByTitles(min, max)

    def getData(self):
        return self.data.getData()