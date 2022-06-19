class FloatValue:
    @classmethod
    def check_value(cls, value):
        if type(value) is not float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.check_value(value)
        instance.__dict__[self.name] = value


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.__N = N
        self.__M = M
        self.cells = list()
        self.create_table()

    def create_table(self):
        for i in range(self.__N):
            self.cells.append([])
            for j in range(self.__M):
                self.cells[i].append(Cell())

    def insert_table(self):
        k = 1
        for i in self.cells:
            for j in i:
                j.value = float(k)
                k += 1


table = TableSheet(5, 3)
table.insert_table()

print(table.cells)
table.insert_table()
print(table.cells)
pass
