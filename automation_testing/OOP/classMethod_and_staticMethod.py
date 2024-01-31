class Book:

    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<-- Book: {self.name}, Book Type: {self.book_type}, Weight: {self.weight} -->"

    """cls = Book. Both are same. Interchangeable. 
    cls more conventional to use"""

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


heavy_book = Book.hardcover('Harry Potter', 1500)
light_book = Book.paperback('Python 101', 800)

print(heavy_book)
print(light_book)