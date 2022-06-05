import random

random.seed(1)


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


def gen_element(n):
    lst = []
    for i in range(n):
        x = random.randint(1, 3)
        arg = (random.randint(0, 999) for i in range(4))
        if x == 1:
            lst.append(Line(*arg))
        elif x == 2:
            lst.append(Rect(*arg))
        elif x == 3:
            lst.append(Ellipse(*arg))
    return lst


elements = gen_element(217)

for i in elements:
    if isinstance(i, Line):
        i.sp = (0, 0)
        i.ep = (0, 0)

for i in elements:
    print(f"name: {i.__class__} {i.__dict__}")
