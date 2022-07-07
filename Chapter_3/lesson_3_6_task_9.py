class Dimensions:
    def __init__(self, a, b, c):
        self.check_value(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.b, self.b, self.c))

    @staticmethod
    def check_value(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")


s_inp = input().split('; ')

lst_dims = sorted([Dimensions(*map(float, elem.split())) for elem in s_inp], key=lambda obj: hash(obj))
