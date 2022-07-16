class Singleton:
    obj = None

    def __new__(cls, *args, **kwargs):
        if Singleton.obj is None:
            Singleton.obj = object.__new__(cls)
        return Singleton.obj


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


obj1 = Game(1)
obj2 = Game(2)

print(obj1.name, obj2.name)
