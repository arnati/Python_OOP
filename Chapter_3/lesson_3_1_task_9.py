class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @classmethod
    def check_value(cls, *args):
        for i in args:
            if i not in (int, float) and not (cls.MIN_DIMENSION <= i <= cls.MAX_DIMENSION):
                return False
        else:
            return True

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        else:
            object.__setattr__(self, key, value)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if self.check_value(a):
            self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        if self.check_value(b):
            self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        if self.check_value(c):
            self.__c = c


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # исключение AttributeError


