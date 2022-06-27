class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        self.__real = real

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        self.__img = img

    def __setattr__(self, key, value):
        if key in ('img', 'real'):
            if type(value) not in (int, float):
                raise ValueError("Неверный тип данных.")
        object.__setattr__(self, key, value)

    def __abs__(self):
        return (self.real ** 2 + self.img ** 2) ** 0.5


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
