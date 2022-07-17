class ListInteger(list):
    def __init__(self, args):
        for i in args:
            self.check_value(i)
        super().__init__(args)

    def append(self, value):
        self.check_value(value)
        super().append(value)

    def check_value(self, args):
        if type(args) is not int:
            raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, key, value):
        self.check_value(value)
        super().__setitem__(key, value)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5  # TypeError
