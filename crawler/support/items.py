class BookItem:
    def __init__(self, name: str, 
                 description: str, 
                 genres: list[str], 
                 author: list[str], 
                 series: str | None):
        self.name = name
        self.description = description
        self.genres = genres
        self.author = author
        self.series = series