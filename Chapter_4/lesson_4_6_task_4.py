from abc import ABC, abstractmethod


class Digit(ABC):
    def __init__(self, value):
        self.check_value(value)
        self.value = value

    @staticmethod
    @abstractmethod
    def check_value(value):
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def check_value(value):
        if type(value) is not int:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def check_value(value):
        if type(value) is not float:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def check_value(value):
        if type(value) not in (int, float) or value < 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def check_value(value):
        if type(value) not in (int, float) or value > 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        Positive.check_value(value)
        super().__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        Positive.check_value(value)
        super().__init__(value)


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))

