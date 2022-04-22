from model.Sportsman import Sportsman
from model.WriterParser import writeXML
from model.ReaderParser import parseXML

class DB:
    def __init__(self):
        self.__data: list[Sportsman] = list()

    def load(self, filepath) -> None:
        self.__data = parseXML(filepath)

    def save(self, filepath) -> None:
        writeXML(filepath, self.__data)

    def getData(self) -> list:
        return self.__data

    def addRecord(self, record: Sportsman) -> None:
        self.__data.append(record)

    def searchByNameOrSport(self, name: str, sport: str) -> list:
        result: list = list()
        for record in self.__data:
            if name in record.name and sport == record.sport:
                result.append(record)
        return result

    def searchByTitles(self, min: int, max: int) -> list:
        result: list = list()
        for record in self.__data:
            if record.titles in range(min, max):
                result.append(record)
        return result

    def searchByNameOrRank(self, name: str, rank: str) -> list:
        result: list = list()
        for record in self.__data:
            if name in record.name and rank == record.rank:
                result.append(record)
        return result

    def deleteByNameOrSport(self, name: str, sport: str) -> int:
        delete = self.searchByNameOrSport(name, sport)
        result = len(delete)
        for element in delete:
            self.__data.remove(element)
        return result

    def deleteByTitles(self, min: int, max: int) -> int:
        delete = self.searchByTitles(min, max)
        result = len(delete)
        for element in delete:
            self.__data.remove(element)
        return result

    def deleteByNameOrRank(self, name: str, rank: str) -> int:
        delete = self.searchByNameOrRank(name, rank)
        result = len(delete)
        for element in delete:
            self.__data.remove(element)
        return result


if __name__ == "__main__":
    data = DB()
    data.load("../examples/db.xml")
    data.save("../examples/db_export.xml")