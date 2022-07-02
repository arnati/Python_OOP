class Lib:
    def __init__(self):
        self.book_list = list()

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.pop(-1)
            return self
        else:
            self.book_list.pop(other)
            return self

    def __len__(self):
        return len(self.book_list)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


book = Book('title', 'author', 'year')
lib = Lib()

lib = lib + book  # добавление новой книги в библиотеку
lib += book

lib = lib - book  # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book

lib = lib - 0  # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= 0
