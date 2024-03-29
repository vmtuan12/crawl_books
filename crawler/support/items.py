class BaseItem:
    def to_json(self) -> dict:
        result = {}
        for attr in self.__dict__:
            result.update({attr: self.__dict__[attr]})

        return result

class BookItem(BaseItem):
    def __init__(self, id: str,
                 name: str, 
                 description: str, 
                 genres: list[str], 
                 author: list[str], 
                 series: str | None, 
                 related_people: list[str] | None,
                 language: str | None,
                 average_rating: float,
                 rating_count: int,
                 num_page: int | None,
                 url: str):
        self.id = id
        self.name = name
        self.description = description
        self.genres = genres
        self.author = author
        self.series = series
        self.related_people = related_people
        self.language = language
        self.average_rating = average_rating
        self.rating_count = rating_count
        self.num_page = num_page
        self.url = url