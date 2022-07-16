class Validator:
    def _is_valid(self, data):
        pass

    def __call__(self, *args, **kwargs):
        if not self._is_valid(args[0]):
            raise ValueError('данные не прошли валидацию')


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) is not int or not (self.min_value <= data <= self.max_value):
            return False
        else:
            return True


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) is not int or not (self.min_value <= data <= self.max_value):
            return False
        else:
            return True
