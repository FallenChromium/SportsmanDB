casts = ["Основной", "Запасной", "N/A"]
ranks = ["1-й юношеский", "2-й разряд",
         "3-й разряд", "Кмс", "Мастер спорта", "Нет"]
fields = ["name", "cast", "position", "titles", "sport", "rank"]
options = {"searchByNameOrSport": "По имени и виду спорта",
           "searchByTitles": "По кол-ву титулов", "searchByNameOrRank": "По имени и разряду"}

class IncorrectFileException(Exception):
    def __str__(self):
        print('Invalid file format!')
