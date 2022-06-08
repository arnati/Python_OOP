class Point:
    x = 0
    y = 0

    def __new__(cls, *args, **kwargs):
        # print(f'конструируем: {args} | {kwargs}')
        cls.x, cls.y = args
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(Point.x, Point.y)


pt = Point(1, 2)
pt_clone = Point.clone(Point)

print(id(pt), id(pt_clone))
