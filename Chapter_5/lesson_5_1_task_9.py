class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self.check_triangle(a, b, c)

    def __setattr__(self, key, value):
        if key in ("_a", "_b", "_c"):
            if type(value) not in (int, float) or value <= 0:
                raise TypeError('стороны треугольника должны быть положительными числами')
        object.__setattr__(self, key, value)

    @staticmethod
    def check_triangle(a, b, c):
        if any(((a >= b + c), (b >= a + c), (c >= a + b))):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = []
for i in input_data:
    try:
        lst_tr.append(Triangle(*i))
    except:
        continue
