class Descriptor:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)

    @classmethod
    def check_value(cls, value):
        if type(value) not in (int, float) or value < 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")


class Triangle:
    a = Descriptor()
    b = Descriptor()
    c = Descriptor()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.check_triangle(a, b, c)

    @classmethod
    def check_triangle(cls, a, b, c):
        if not (a < b + c and b < a + c and c < a + b):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return self.a + self.b + self.c

    def tr(self):
        p = len(self) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def __call__(self, *args, **kwargs):
        return self.tr()
