class PathLines:
    def __init__(self, *args):
        self.lst = list(args)

    def get_path(self):
        return self.lst

    def get_length(self):
        length = 0
        x0 = 0
        y0 = 0
        for obj in self.lst:
            length += ((obj.x - x0) ** 2 + (obj.y - y0) ** 2) ** 0.5
            x0 = obj.x
            y0 = obj.y

        return length

    def add_line(self, line):
        self.lst.append(line)


class LineTo:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()

print(dist)
