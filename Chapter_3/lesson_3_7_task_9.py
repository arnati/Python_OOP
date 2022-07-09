class Vector:
    def __init__(self, *args):
        self.args = args

    @staticmethod
    def check_value(obj1, obj2):
        if len(obj1.args) != len(obj2.args):
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        self.check_value(self, other)
        return Vector(*(self.args[i] + other.args[i] for i in range(len(self.args))))

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.args = tuple(self.args[i] + other.args[i] for i in range(len(self.args)))
        else:
            self.args = tuple(self.args[i] + other for i in range(len(self.args)))

        return self

    def __sub__(self, other):
        self.check_value(self, other)
        return Vector(*(self.args[i] - other.args[i] for i in range(len(self.args))))

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.args = tuple(self.args[i] - other.args[i] for i in range(len(self.args)))
        else:
            self.args = tuple(self.args[i] - other for i in range(len(self.args)))

        return self

    def __mul__(self, other):
        self.check_value(self, other)
        return Vector(*(self.args[i] * other.args[i] for i in range(len(self.args))))

    def __eq__(self, other):
        if len(self.args) != len(other.args):
            return False

        for i in range(len(self.args)):
            if self.args[i] != other.args[i]:
                return False
        else:
            return True


v1 = Vector(1, 2, 3)
v1 += 10
pass
