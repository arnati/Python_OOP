class Ellipse:
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        if None not in [x1, y1, x2, y2]:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

        self.args = [x1, y1, x2, y2]
        self.args = [i for i in self.args if i is not None]

    def __bool__(self):
        return True if len(self.args) == 4 else False

    def get_coords(self):
        if bool(self):
            return tuple(self.args)
        raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for obj in lst_geom:
    if bool(obj):
        obj.get_coords()
