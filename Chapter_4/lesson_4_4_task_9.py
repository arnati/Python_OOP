class class_log:
    def __init__(self, vector_log):
        self.vector_log = vector_log

    def __call__(self, dec_class):
        def wrapper(*args, **kwargs):
            methods = {k: v for k, v in dec_class.__dict__.items() if callable(v)}
            for k, v in methods.items():
                setattr(dec_class, k, self.set_new_func(v))
            return dec_class(*args)

        return wrapper

    def set_new_func(self, func):
        def wrapper(*args, **kwargs):
            self.vector_log.append(func.__name__)
            return func(*args, **kwargs)
        return wrapper


vector_log = [] # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
pass
