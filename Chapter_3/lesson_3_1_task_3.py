class Book:
    title = ''
    author = ''
    pages = 0
    year = 0

    def __init__(self, title="", author="", pages=0, year=0):
        Book.title = title
        Book.author = author
        Book.pages = pages
        Book.year = year

        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    @classmethod
    def __setattr__(cls, key, value):
        # print(key, value)
        if key in ('title', 'author'):
            if type(value) is not str:
                raise TypeError("Неверный тип присваиваемых данных.")
        else:
            if type(value) is not int:
                raise TypeError("Неверный тип присваиваемых данных.")


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)

assert book.title == "Python ООП"
assert book.author == "Сергей Балакирев"
assert book.pages == 123
assert book.year == 2022

print(book.title)
