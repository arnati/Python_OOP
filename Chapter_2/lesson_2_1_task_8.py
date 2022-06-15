class Point:
    def __init__(self, x, y):
        if self.check_value(x, y):
            self.__x = x
            self.__y = y

    @staticmethod
    def check_value(x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            return True
        return False

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2 and Point in args:
            self.__sp = args[0]
            self.__ep = args[1]
        elif len(args) == 4:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f"Прямоугольник с координатами: {self.get_coords()[0].get_coords()} {self.get_coords()[1].get_coords()}")


rect = Rectangle(0, 0, 20, 34)
