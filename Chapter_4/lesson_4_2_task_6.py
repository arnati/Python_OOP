class Tuple(tuple):
    def __init__(self, iter_obj):
        self.iter_obj = tuple(iter_obj)

    def __add__(self, other):
        return Tuple(self.iter_obj + tuple(other))



t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"

pass