class Book:
    def __init__(self, title, publisher, authors, genres, copies, max_renewals=5):
        self.title = title
        self.publisher = publisher
        self.authors = authors
        self.genres = genres
        self.copies = []
        self.max_renewals = max_renewals

    def __repr__(self):
        return f"Book({self.id}, '{self.title}', '{self.authors}', '{self.genres}', {self.copies}, {self.max_renewals})"
