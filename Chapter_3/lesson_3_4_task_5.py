class ListMath:
    def __init__(self, *args):
        if len(args) == 0:
            self.lst_math = list()
        else:
            self.lst_math = list(filter(lambda x: True if type(x) in (int, float) else False, list(args[0])))

    def __add__(self, other):
        return ListMath([elem + other for elem in self.lst_math])

    def __iadd__(self, other):
        self.lst_math = [elem + other for elem in self.lst_math]
        return self

    def __sub__(self, other):
        return ListMath([elem - other for elem in self.lst_math])

    def __isub__(self, other):
        self.lst_math = [elem - other for elem in self.lst_math]
        return self

    def __rsub__(self, other):
        return ListMath([other - elem for elem in self.lst_math])

    def __mul__(self, other):
        return ListMath([elem * other for elem in self.lst_math])

    def __imul__(self, other):
        self.lst_math = [elem * other for elem in self.lst_math]
        return self

    def __rmul__(self, other):
        return ListMath([other * elem for elem in self.lst_math])

    def __truediv__(self, other):
        return ListMath([elem / other for elem in self.lst_math])

    def __itruediv__(self, other):
        self.lst_math = [elem / other for elem in self.lst_math]
        return self


lst = ListMath([1, "abc", -5, 7.68, True])

lst = lst + 76  # сложение каждого числа списка с определенным числом
lst += 76  # сложение каждого числа списка с определенным числом
pass
lst = lst - 76  # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst  # вычитание из числа каждого числа списка
lst -= 76.3
pass
lst = lst * 5  # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst  # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
pass
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst /= 13.0
