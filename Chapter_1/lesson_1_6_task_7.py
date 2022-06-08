class SingletonFive:
    num_obj = 0
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.num_obj < 5:
            cls.num_obj += 1
            cls.obj = super().__new__(cls)
            return cls.obj
        return cls.obj

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]

