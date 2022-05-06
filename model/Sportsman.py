from model.constants import casts, ranks, IncorrectFileException
class Sportsman:
    def __init__(self, name, cast: str, position: str, titles: str, sport: str, rank: str) -> None:
        if cast not in casts or rank not in ranks:
            raise IncorrectFileException()
        self.name = name
        self.cast = cast
        self.position = int(position)
        self.titles = int(titles)
        self.sport = sport
        self.rank = rank

    def __len__(self) -> int:
        return 6
