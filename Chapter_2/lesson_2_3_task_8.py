class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.__min_length = min_length
        self.__max_length = max_length

    def check_value(self, string):
        if type(string) is str and self.__min_length <= len(string) <= self.__max_length:
            return True
        return False

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_value(value):
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_value=10000):
        self.__max_value = max_value

    def check_value(self, x):
        if type(x) in (int, float) and 0 <= x <= self.__max_value:
            return True
        return False

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_value(value):
            setattr(instance, self.name, value)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
