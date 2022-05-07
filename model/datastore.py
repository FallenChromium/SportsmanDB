from model.Sportsman import Sportsman
from model.WriterParser import writeXML
from model.ReaderParser import parseXML
from model.constants import ranks, casts

class DataStore:
    def __init__(self):
        self.__data: list[Sportsman] = list()

    def load(self, filepath) -> None:
        self.__data = parseXML(filepath)

    def save(self, filepath) -> None:
        writeXML(filepath, self.__data)

    def getData(self) -> list:
        return self.__data

    def addRecord(self, record: Sportsman) -> int:
        self.__data.append(record)
        return len(self.__data)

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
    
    def sportsList(self) -> list[str]:
        return list(set([sportsman.sport for sportsman in self.__data]))

    def ranksList(self) -> list[str]:
        return ranks
    
    def castsList(self) -> list[str]:
        return casts


if __name__ == "__main__":
    data = DataStore()
    data.load("../examples/db.xml")
    data.save("../examples/db_export.xml")