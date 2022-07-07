import sys


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name, self.author))


# lst_in = [
#     'Python; Балакирев С.М.; 2020',
#     'Python ООП; Балакирев С.М.; 2021',
#     'Python ООП; Балакирев С.М.; 2022',
#     'Python; Балакирев С.М.; 2021'
# ]
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_bs = [BookStudy(*row.split('; ')) for row in lst_in]
unique_books = len(set(obj_hash.__hash__() for obj_hash in lst_bs))
