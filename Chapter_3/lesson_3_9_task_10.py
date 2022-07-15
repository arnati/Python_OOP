class Matrix:
    def __init__(self, *args):
        self.max_rows = 0
        self.max_cols = 0

        if len(args) > 1:
            check = all(
                (type(args[0]) is int, type(args[1]) is int, args[0] >= 0, args[1] >= 0, type(args[2]) in (int, float)))
            if check:
                self.rows = args[0]
                self.cols = args[1]
                self.fill_value = args[2]
                self.list2D = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]

                self.max_rows = self.rows
                self.max_cols = self.cols
            else:
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
        else:
            b = args[0][0]
            check_row = len(args[0][0])
            for row in args[0]:
                if len(row) != check_row:
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')
                for elem in row:
                    if not bool(type(elem) in (int, float)):
                        raise TypeError('список должен быть прямоугольным, состоящим из чисел')
                self.list2D = args[0]
                self.max_rows = len(self.list2D)
                self.max_cols = len(self.list2D[0])

    def __getitem__(self, item):
        self.check_index(item)
        return self.list2D[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.check_index(key)
        if type(value) in (int, float):
            self.list2D[key[0]][key[1]] = value
        else:
            raise TypeError('значения матрицы должны быть числами')

    def check_index(self, index):
        if not (0 <= index[0] < self.max_rows) or not (0 <= index[1] < self.max_cols):
            raise IndexError('недопустимые значения индексов')

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.max_rows == other.max_rows and self.max_cols == other.max_cols:
                return Matrix(
                    [[self.list2D[row][col] + other.list2D[row][col] for col in range(self.max_cols)] for row in
                     range(self.max_rows)])
            else:
                raise ValueError('операции возможны только с матрицами равных размеров')
        else:
            return Matrix([[elem + other for elem in row] for row in self.list2D])

    def __radd__(self, other):
        return Matrix([[elem + other for elem in row] for row in self.list2D])

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.max_rows == other.max_rows and self.max_cols == other.max_cols:
                return Matrix(
                    [[self.list2D[row][col] - other.list2D[row][col] for col in range(self.max_cols)] for row in
                     range(self.max_rows)])
            else:
                raise ValueError('операции возможны только с матрицами равных размеров')
        else:
            return Matrix([[elem - other for elem in row] for row in self.list2D])

    def __rsub__(self, other):
        return Matrix([[other - elem for elem in row] for row in self.list2D])


mt1 = Matrix([[1, 2], [3, 4]])
mt2 = Matrix([[1, 2], [3, 4]])
mt3 = mt2 - mt1

pass