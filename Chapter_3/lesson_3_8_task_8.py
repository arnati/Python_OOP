class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.value = 0
                cell.is_free = False

    def __getitem__(self, item):
        self.check_index(item)
        if isinstance(item, tuple):
            if slice in (type(item[0]), type(item[1])):
                if type(item[0]) is slice:  # столбец
                    rows = self.pole[item[0]]
                    return tuple(row[item[1]].value for row in rows)
                else:
                    row = self.pole[item[0]]
                    return tuple(cell.value for cell in row[item[1]])

            else:
                return self.pole[item[0]][item[1]].value
        else:
            return self.pole[item].value

        # return self.pole[item[0]][item[1]].value if isinstance(item, tuple) else self.pole[item].value

    def check_index(self, index):
        if slice in (type(index[0]), type(index[1])):
            if type(index[0]) is slice:
                if not (0 <= index[1] < len(self.pole[0])):  # строки
                    IndexError('некорректный индекс')
            else:
                if not (0 <= index[0] < len(self.pole)):  # столбцы
                    IndexError('некорректный индекс')
        else:
            a = isinstance(index[0], int)
            b = 0 <= index[0] < len(self.pole)
            c = isinstance(index[1], int)
            d = 0 <= index[1] < len(self.pole[0])
            if not all((a, b, c, d)):
                raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        self.check_index(key)

        if not self.pole[key[0]][key[1]]:
            self.pole[key[0]][key[1]].value = value
            self.pole[key[0]][key[1]].is_free = True
        else:
            raise ValueError('клетка уже занята')


class Cell:
    def __init__(self):
        self.is_free = False
        self.value = 0

    def __bool__(self):
        return self.is_free


game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
# # формируется поле:
# # 1 0 0
# # 2 0 0
# # 0 0 0
# # game[3, 2] = 2 # генерируется исключение IndexError
# if game[0, 0] == 0:
#     game[0, 0] = 2
# v1 = game[0, :]  # 1, 0, 0
# v2 = game[:, 0]  # 1, 2, 0
# game.clear()
# v3 = game[0, :]  # 1, 0, 0
# v4 = game[:, 0]  # 1, 2, 0


game.clear()
game[0, 0] = 1
game[1, 0] = 2
game[2, 0] = 3

v5 = game[0, :]
v6 = game[1, :]
v7 = game[:, 0]

pass
