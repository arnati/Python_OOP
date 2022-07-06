class Box:
    def __init__(self):
        self.lst = list()

    def add_thing(self, obj):
        self.lst.append(obj)

    def get_things(self):
        return self.lst

    def __eq__(self, other):
        if len(self.lst) != len(other.lst):
            return False

        for thing in self.lst:
            if thing not in other.lst:
                return False
            elif thing != other.lst[other.lst.index(thing)]:
                return False
        else:
            return True


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return True if self.mass == other.mass and self.name.lower() == other.name.lower() else False


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2  # True
pass