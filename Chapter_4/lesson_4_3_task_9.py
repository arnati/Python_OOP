class StringDigit(str):
    def __init__(self, string):
        self.check_value(string)
        self.string = string

    @staticmethod
    def check_value(string):
        for i in string:
            if not i.isdigit():
                raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        res = self.string + other
        self.check_value(res)
        return StringDigit(res)

    def __radd__(self, other):
        res = other + self.string
        self.check_value(res)
        return StringDigit(res)


sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
sd = sd + "12f" # ValueError

pass