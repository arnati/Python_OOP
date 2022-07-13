class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.lst = list()
        self.current_weight = 0

    def add_thing(self, thing):
        self.check_weight(thing)
        self.lst.append(thing)
        self.current_weight += thing.weight

    def check_weight(self, thing):
        if not (self.current_weight + thing.weight) <= self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def check_index(self, index):
        if not (isinstance(index, int)) or not (0 <= index < len(self.lst)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_index(item)
        return self.lst[item]

    def __setitem__(self, key, value):
        self.check_index(key)

        self.current_weight -= self.lst[key].weight
        self.check_weight(value)

        self.lst[key] = value
        self.current_weight += value.weight

    def __delitem__(self, key):
        self.check_index(key)
        self.current_weight -= self.__getitem__(key).weight
        self.lst.pop(key)


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300))  # генерируется исключение ValueError
print(bag[2].name)  # рубашка
bag[0] = Thing('платок', 150)
bag[1] = Thing('платок', 333)
bag[2] = Thing('платок', 333)
print(bag[1].name)  # латок
del bag[0]
print(bag[0].name)  # платок
# t = bag[4]  # генерируется исключение IndexError
