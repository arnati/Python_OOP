class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class CellInteger:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self.check_value(value)
        self._value = value

    def check_value(self, value):
        if type(value) is not int or not (self._min_value <= value <= self._max_value):
            raise CellIntegerException('значение выходит за допустимый диапазон')


class CellFloat(CellInteger):
    def check_value(self, value):
        if type(value) is not float or not (self._min_value <= value <= self._max_value):
            raise CellFloatException('значение выходит за допустимый диапазон')


class CellString:
    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self.check_value(value)
        self._value = value

    def check_value(self, value):
        if type(value) is not str or not (self._min_length <= len(value) <= self._max_length):
            raise CellStringException('длина строки выходит за допустимый диапазон')


class TupleData:
    def __init__(self, *args):
        self.lst = list(args)

    def __getitem__(self, item):
        self.check_index(item)
        return self.lst[item].value

    def __setitem__(self, key, value):
        self.check_index(key)
        self.lst[key].value = value

    def check_index(self, index):
        if type(index) is not int or not (0 <= index < len(self.lst)):
            raise IndexError

    def __len__(self):
        return len(self.lst)

    def __iter__(self):
        for obj in self.lst:
            yield obj.value


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
