# Class inheritance means a book is a bookshelf
# Class composition means a bookshelf has number of books
class Bookshelf:

    def __init__(self, *books):

        """*book is here an *args both same thing"""
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} Books."


class Book:

    """No need for inheritance here"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book('Harry Potter')
book1 = Book('Python 101')
shelf = Bookshelf(book, book1)

print(shelf)