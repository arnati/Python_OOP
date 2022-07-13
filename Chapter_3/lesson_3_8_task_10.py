class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.dict_table = dict()

    def update_attr(self):
        r = max(set((row[0] for row in self.dict_table.keys())))
        c = max(set((col[1] for col in self.dict_table.keys())))
        self.rows = 0 if r == 0 else r + 1
        self.cols = 0 if c == 0 else c + 1

    def add_data(self, row, col, data):
        self.dict_table[(row, col)] = data
        self.update_attr()

    def remove_data(self, row, col):
        self.check_key_dict((row, col))
        self.dict_table.pop((row, col))
        self.update_attr()

    def check_key_dict(self, key):
        if key not in self.dict_table.keys():
            raise IndexError('ячейка с указанными индексами не существует')

    def __getitem__(self, item):
        self.check_index(item)
        return self.dict_table[item].value

    def __setitem__(self, key, value):
        self.dict_table[key] = Cell(value)
        self.update_attr()

    def check_index(self, index):
        if index not in self.dict_table.keys():
            raise ValueError('данные по указанным индексам отсутствуют')


class Cell:
    def __init__(self, value):
        self.value = value


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25  # изменение значения существующей ячейки
st[11, 7] = 'cell_117'  # создание новой ячейки
print(st[0, 0])  # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols)  # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError
