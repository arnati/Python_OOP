class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = list()
        self.current_weight = 0

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if (self.current_weight + thing.weight) <= self.max_weight:
            self.__things.append(thing)
            self.current_weight += thing.weight

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        return self.current_weight


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")
