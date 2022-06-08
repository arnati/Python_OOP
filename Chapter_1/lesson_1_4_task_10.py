import random


# random.seed(1)


class Cell:
    def __init__(self, mine, around_mines=0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.pole = list()
        self.n = N
        self.m = M

    def init(self):
        mine = set()
        while len(mine) != self.m:
            mine.add((random.randint(0, self.n - 1), random.randint(0, self.n - 1)))

        for i in range(self.n):
            self.pole.append([])
            for j in range(self.n):
                if (i, j) in mine:
                    self.pole[i].append(Cell(True))
                else:
                    self.pole[i].append(Cell(False))

    def around_mines(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.pole[i][j].mine:
                    if j - 1 >= 0 and not self.pole[i][j - 1].mine:
                        self.pole[i][j - 1].around_mines += 1

                    if (i - 1 >= 0 and j - 1 >= 0) and not self.pole[i - 1][j - 1].mine:
                        self.pole[i - 1][j - 1].around_mines += 1

                    if i - 1 >= 0 and j - 1 >= 0 and not self.pole[i - 1][j].mine:
                        self.pole[i - 1][j].around_mines += 1

                    if (i - 1 >= 0 and j + 1 < self.n) and not self.pole[i - 1][j + 1].mine:
                        self.pole[i - 1][j + 1].around_mines += 1

                    if j + 1 < self.n and not self.pole[i][j + 1].mine:
                        self.pole[i][j + 1].around_mines += 1

                    if (i + 1 < self.n and j + 1 < self.n) and not self.pole[i + 1][j + 1].mine:
                        self.pole[i + 1][j + 1].around_mines += 1

                    if i + 1 < self.n and not self.pole[i + 1][j].mine:
                        self.pole[i + 1][j].around_mines += 1

                    if (i + 1 < self.n and j - 1 >= 0) and not self.pole[i + 1][j - 1].mine:
                        self.pole[i + 1][j - 1].around_mines += 1

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.pole[i][j].mine:
                    print('*', end=' ')
                else:
                    print(self.pole[i][j].around_mines, end=' ')
            print()


pole_game = GamePole(10, 12)
pole_game.init()
pole_game.around_mines()

pole_game.show()
