class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __setattr__(self, key, value):
        if key in ("_x", "_y"):
            if type(value) not in (int, float):
                raise ValueError('некорректные координаты и параметры прямоугольника')
        elif key in ("_width", "_height"):
            if type(value) not in (int, float) or value <= 0:
                raise ValueError('некорректные координаты и параметры прямоугольника')
        object.__setattr__(self, key, value)

    def is_collision(self, rect):
        left_top = (rect.x, rect.y)
        right_top = (rect.x + rect.width, rect.y)
        right_down = (rect.x + rect.width, rect.y - rect.height)
        left_down = (rect.x, rect.y - rect.height)
        lst = (left_top, right_top, right_down, left_down)

        for points in lst:
            self.check_coord(points)

    def check_coord(self, coord):
        if self.x <= coord[0] <= self.x + self.width and self.y - self.height <= coord[1] <= self.y:
            raise TypeError('прямоугольники пересекаются')


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]

lst_not_collision = []

for obj1 in lst_rect:
    try:
        for obj2 in lst_rect:
            if obj2 != obj1:
                obj1.is_collision(obj2)
        lst_not_collision.append(obj1)
    except:
        continue
