class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def volume(self):
        return self.a * self.b * self.c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    def __setattr__(self, key, value):
        if key in ('a', 'b', 'c'):
            if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
                return object.__setattr__(self, key, value)
        else:
            return object.__setattr__(self, key, value)

    def __ge__(self, other):
        v1 = self.a * self.b * self.c
        v2 = other.a * other.b * other.c
        return True if v1 >= v2 else False

    def __gt__(self, other):
        v1 = self.a * self.b * self.c
        v2 = other.a * other.b * other.c
        return True if v1 > v2 else False


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume())
