import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for i in data:
            id, name, old, salary = i.split()
            self.lst_data.append(dict({'id': id, 'name': name, 'old': old, 'salary': salary}))

    def select(self, a, b):
        return self.lst_data[a:b + 1]


db = DataBase()
db.insert(lst_in)
# print(db.select(0, 2))
