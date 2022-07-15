class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    def get_info(self):
        lst = list(self.__dict__.values())
        return f"{lst[0]}: {lst[1]}, {', '.join(map(str, lst[2:]))}"


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size


cat = Cat('cat', 5, 'green', 2)
cat.get_info()
Dog('пёс', 4, 'хаски', (2, 3)).get_info()
