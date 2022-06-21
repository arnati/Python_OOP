class Circle:
    def __init__(self, x, y, radius):
        self.check_value(x, y, radius)
        self.__x = x
        self.__y = y
        self.__radius = radius

    @staticmethod
    def check_value(x, y, radius):
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")

        if type(radius) not in (int, float) or radius < 0:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def __setattr__(self, key, value):
        # if key in ('_Circle__x', '_Circle__y'):
        #     if type(value) not in (int, float):
        #         raise TypeError("Неверный тип присваиваемых данных.")
        #     else:
        #         object.__setattr__(self, key, value)
        # elif key == '_Circle__radius':
        #     if type(value) not in (int, float):
        #         raise TypeError("Неверный тип присваиваемых данных.")
        #     elif value > 0:
        #         object.__setattr__(self, key, value)

        if key in ('x', 'y'):
            if type(value) not in (int, float):
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)
        elif key == 'radius':
            if type(value) not in (int, float):
                raise TypeError("Неверный тип присваиваемых данных.")
            elif value > 0:
                object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        if item not in self.__dict__.keys():
            return False


circle = Circle(10.5, 7, -22)
circle.radius = 100  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name  # False, т.к. атрибут name не существует
pass
