class Author:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Author: {self.name}"

    def __repr__(self):
        return f"Author('{self.name}')"


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f"Book: {self.name} ({self.year}), {self.author}"

    def __repr__(self):
        return f"Book('{self.name}', {self.year}, {repr(self.author)})"


class Library:
    def __init__(self):
        self.books = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]


author1 = Author("Alfred Hitchcock")
author2 = Author("Agata Christie")

library = Library()
library.new_book("witch brew", 1976, author1)
library.new_book("monster museum", 1965, author1)
library.new_book("Nemesis", 1971, author2)

print(library.group_by_author(author1))
print(library.group_by_year(1971))
