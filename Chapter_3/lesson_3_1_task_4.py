class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id = 0

    def __new__(cls, *args, **kwargs):
        cls.id += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.id = self.id
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        # print(key, value)
        if key == 'id':
            if type(value) is not int:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)
        elif key == 'name':
            if type(value) is not str:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)
        elif key == 'weight':
            if (type(value) not in (int, float)) or value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)
        elif key == 'price':
            if type(value) not in (int, float) or value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
# book.__delattr__('weight')
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")

print(shop.goods)
shop.remove_product(book)
print(shop.goods)