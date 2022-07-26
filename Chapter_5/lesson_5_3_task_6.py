class TupleLimit(tuple):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, args)

    def __init__(self, lst, max_length):
        if len(lst) <= max_length:
            self.lst = lst
        else:
            raise ValueError('число элементов коллекции превышает заданный предел')

    def __str__(self):
        return ' '.join(map(str, self.lst))


try:
    digits = list(map(float, input().split()))
    t = TupleLimit(digits, 5)
    print(t)
except Exception as e:
    print(e)
