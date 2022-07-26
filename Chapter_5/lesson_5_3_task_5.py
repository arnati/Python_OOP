class Test:
    def __init__(self, descr):
        self.check_value(descr)
        self.descr = descr

    def check_value(self, descr):
        if not isinstance(descr, str) or not (10 <= len(descr) <= 10000):
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def __setattr__(self, key, value):
        if key in ("ans_digit", "max_error_digit"):
            if type(value) not in (int, float):
                raise ValueError('недопустимые значения аргументов теста')
            if key == "max_error_digit" and value < 0:
                raise ValueError('недопустимые значения аргументов теста')
        object.__setattr__(self, key, value)

    def run(self):
        ans = float(input())
        if self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit:
            return True
        return False


try:
    descr, ans = map(str.strip, input().split('|'))
    ans = float(ans)
    t = TestAnsDigit(descr, ans)
    print(t.run())
except Exception as e:
    print(e)


