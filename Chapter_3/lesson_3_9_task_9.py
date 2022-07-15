class TableValues:
    type_data = int

    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.dict_table = [[Cell() for _ in range(cols)] for _ in range(rows)]

    def check_value(self, cords):
        if type(cords[0]) is not int or type(cords[1]) is not int \
                or not (0 <= cords[0] < self.rows) or not (0 <= cords[1] < self.cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_value(item)
        res = self.dict_table[item[0]][item[1]]
        return res.data if res else res

    def __setitem__(self, key, value):
        self.check_value(key)
        self.dict_table[key[0]][key[1]].data = value

    def __iter__(self):
        for row in self.dict_table:
            yield [0 if elem == 0 else elem.data for elem in row]


class Cell:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if type(data) is TableValues.type_data:
            self.__data = data
        else:
            raise TypeError('неверный тип присваиваемых данных')


table = TableValues(5, 5)

c1 = Cell(1)
c2 = Cell(2)
c3 = Cell(3)

table[1, 1] = True
print(table[1, 1])

for row in table:  # перебор по строкам
    for value in row:  # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
