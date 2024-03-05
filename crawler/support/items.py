class BaseItem:
    def to_json(self) -> dict:
        result = {}
        for attr in self.__dict__:
            result.update({attr: self.__dict__[attr]})

        return result

class BookItem(BaseItem):
    def __init__(self, name: str, 
                 description: str, 
                 genres: list[str], 
                 author: list[str], 
                 series: str | None, 
                 related_people: dict | None,
                 url: str):
        self.name = name
        self.description = description
        self.genres = genres
        self.author = author
        self.series = series
        self.related_people = related_people
        self.url = url