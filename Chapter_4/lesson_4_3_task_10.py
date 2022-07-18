class ItemAttrs:
    def __getitem__(self, item):
        return list(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        key_dict = list(self.__dict__.keys())[key]
        self.__dict__[key_dict] = value


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1, 2.5)
x = pt[0]  # 1
y = pt[1]  # 2.5
pt[0] = 10

pass
