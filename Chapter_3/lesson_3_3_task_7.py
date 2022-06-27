class RadiusVector:
    def __init__(self, *args):
        self.lst = list()
        if len(args) == 1:
            self.lst = [0 for i in range(args[0])]
        else:
            self.lst = list(args)

    def set_coords(self, *args):
        for id, value in enumerate(list(args)):
            if id < len(self.lst):
                self.lst[id] = value

    def get_coords(self):
        return tuple(self.lst)

    def __len__(self):
        return len(self.lst)

    def __abs__(self):
        s = 0
        for i in self.lst:
            s += i ** 2
        return s ** 0.5


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)

print(vector3D.get_coords())
pass
