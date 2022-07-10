class Array:
    def __init__(self, max_length, cell):
        self.lst = [cell() for _ in range(max_length)]

    def __getitem__(self, item):
        if not isinstance(item, int) or not (0 <= item < len(self.lst)):
            raise IndexError('некорректный индекс')
        return self.lst[item].value

    def __setitem__(self, key, value):
        if not isinstance(key, int) or not (0 <= key < len(self.lst)):
            raise IndexError('некорректный индекс')
        self.lst[key].value = value

    def __str__(self):
        return ' '.join(map(lambda obj: str(obj.value), self.lst))


class Integer:
    def __init__(self, start_value=0):
        self.__cell_value = start_value

    @property
    def value(self):
        return self.__cell_value

    @value.setter
    def value(self, value):
        if type(value) is not int:
            raise ValueError('должно быть целое число')
        self.__cell_value = value


ar_int = Array(10, cell=Integer)
print(ar_int[3])
a = ar_int
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1 # должно генерироваться исключение IndexError
print(ar_int)
