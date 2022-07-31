import copy


class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._current_weight = 0
        self._things = list()

    def add_thing(self, obj):
        self.check_weight(obj)
        self._things.append(obj)
        self._current_weight += obj[1]

    def check_weight(self, obj):
        if obj[1] + self._current_weight > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')


class BoxDefender:
    def __init__(self, obj):
        self.link_obj = obj

    def __enter__(self):
        self.temp_obj = copy.deepcopy(self.link_obj)
        return self.temp_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.link_obj.__dict__.update(self.temp_obj.__dict__)
        return False


b = Box('name', 2000)
assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"

b.add_thing(("1", 100))
b.add_thing(("2", 200))

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 1000))
        bb.add_thing(("4", 1900))
except ValueError:
    assert len(b._things) == 2

else:
    assert False, "не сгенерировалось исключение ValueError"
