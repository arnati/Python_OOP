class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.check_value(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.check_value(y):
            self.__y = y

    @classmethod
    def check_value(cls, x):
        if cls.MIN_COORD <= x <= cls.MAX_COORD:
            return True
        return False

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2
