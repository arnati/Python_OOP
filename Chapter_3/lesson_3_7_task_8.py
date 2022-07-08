import random


# random.seed(1)


class GamePole:
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = super().__new__(cls)

        return cls.obj

    def __init__(self, N, M, total_mines):
        self.n = N
        self.m = M
        self.total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(self.m)) for _ in range(self.n))

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        coordinates_mine = set()
        while len(coordinates_mine) != self.total_mines:
            coordinates_mine.add((random.randint(0, self.n - 1), random.randint(0, self.m - 1)))

        for coord in coordinates_mine:
            self.pole[coord[0]][coord[1]].is_mine = True

        self.around_mines()

    def around_mines(self):
        top = down = tuple(((0,) * (self.m + 2),))
        temp_pole = ()
        for row in self.pole:
            temp_pole += ((0,) + row + (0,)),

        temp_pole = top + temp_pole + down

        for row_id in range(1, self.n + 1):
            for cell_id in range(1, self.m + 1):
                if not temp_pole[row_id][cell_id].is_mine:
                    # print((row_id, coll_id))
                    sum_mine = sum(temp_pole[row_id - 1][cell_id - 1:cell_id + 2]) + \
                               sum(temp_pole[row_id][cell_id - 1:cell_id + 2]) + \
                               sum(temp_pole[row_id + 1][cell_id - 1:cell_id + 2])

                    self.pole[row_id - 1][cell_id - 1].number = sum_mine

    def open_cell(self, i, j):
        if 0 <= i <= self.n - 1 and 0 <= j <= self.m - 1:
            self.pole[i][j].is_open = True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self, show=False):
        for row in self.pole:
            for mine in row:
                if mine.is_mine:
                    if show:
                        print('*', end=' ')
                    else:
                        print('?', end=' ')
                else:
                    if show:
                        print(mine.number, end=' ')
                    else:
                        print('?', end=' ')
            print()


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, is_mine):
        self.__is_mine = is_mine

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, is_open):
        self.__is_open = is_open

    def __setattr__(self, key, value):
        if key in ("is_mine", "is_open"):
            if type(value) is not bool:
                raise ValueError("недопустимое значение атрибута")
        elif key == "number":
            if type(value) is not int or not (0 <= value <= 8):
                raise ValueError("недопустимое значение атрибута")

        return object.__setattr__(self, key, value)

    def __bool__(self):
        return False if self.is_open else True

    def __add__(self, other):
        return self.is_mine + other

    def __radd__(self, other):
        return self.is_mine + other


pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole.init_pole()
# if pole.pole[0][1]:
#     pole.open_cell(0, 1)
# if pole.pole[3][5]:
#     pole.open_cell(3, 5)
# # pole.open_cell(30, 100)  # генерируется исключение IndexError
# pole.show_pole(True)

c = Cell()
# c.is_open = 1
# c.is_open = 0
# c.is_open = 'True'

# c.is_mine = '1'
c.number = 9
