class Track:
    def __init__(self, *args):
        self.__points = list(args)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __setattr__(self, key, value):
        if key in ('_x', '_y'):
            if type(value) not in (int, float):
                raise TypeError('координаты должны быть числами')
        object.__setattr__(self, key, value)

    def __str__(self):
        return f"PointTrack: {self._x}, {self._y}"


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
