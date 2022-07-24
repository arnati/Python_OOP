class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value, *args, **kwargs):
        self.check_value(value)

    def check_value(self, value):
        if type(value) is not float or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


class IntegerValidator(FloatValidator):
    def check_value(self, value):
        if type(value) is not int or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


def is_valid(lst, validators):
    lst_res = []
    for elem in lst:
        for validator in validators:
            try:
                validator(elem)
                lst_res.append(elem)
            except:
                continue
    return lst_res


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]

pass
