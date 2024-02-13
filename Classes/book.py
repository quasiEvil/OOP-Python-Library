class Book:
    # inventory = []
    # id = 1

    def __init__(self, title, publisher, authors, genres, copies, max_renewals=5):
        self.title = title
        # self.id = Book.id
        # Book.id += 1
        self.publisher = publisher
        self.authors = authors
        self.genres = genres
        self.copies = []
        self.max_renewals = max_renewals

        # Adds each copy to the inventory

    #     Book.inventory.append(self)

    # def add_copy(self, book_copy):
    #     self.copies.append(book_copy)

    def __repr__(self):
        return f"Book({self.id}, '{self.title}', '{self.authors}', '{self.genres}', {self.copies}, {self.max_renewals})"
