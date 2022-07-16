class Vector:
    def __init__(self, *args):
        self.coord = args

    def __add__(self, other):
        self.check_value(other)
        return Vector(*(self.coord[x] + other.coord[x] for x in range(len(self.coord))))

    def __sub__(self, other):
        self.check_value(other)
        return Vector(*(self.coord[x] - other.coord[x] for x in range(len(self.coord))))

    def check_value(self, other):
        if len(self.coord) != len(other.coord):
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return self.coord


class VectorInt(Vector):
    def __init__(self, *args):
        self.check_type(args)
        super().__init__(*args)

    def check_type(self, args):
        for i in args:
            if type(i) is not int:
                raise ValueError('координаты должны быть целыми числами')

    def __add__(self, other):
        self.check_value(other)
        res = [self.coord[x] + other.coord[x] for x in range(len(self.coord))]
        type_res = False if float in (type(i) for i in res) else True
        return VectorInt(*res) if type_res else Vector(*res)

    def __sub__(self, other):
        self.check_value(other)
        res = [self.coord[x] + other.coord[x] for x in range(len(self.coord))]
        type_res = False if float in (type(i) for i in res) else True
        return VectorInt(*res) if type_res else Vector(*res)


v1 = Vector(0.5, 2, 3)
v2 = VectorInt(3, 4, 5)

v3 = v1 + v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
v4 = v1 - v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами

pass
