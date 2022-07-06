import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.total = 1

    def __eq__(self, other):
        if self.__hash__() == other.__hash__():
            self.total += 1
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))


# lst_in = [
#     'Системный блок: 1500 75890.56',
#     'Монитор Samsung: 2000 34000',
#     'Клавиатура: 200.44 545',
#     'Монитор Samsung: 2000 34000'
# ]
lst_in = list(map(str.strip, sys.stdin.readlines()))

shop_items = {ShopItem(row.split(':')[0], row.split(':')[1].split()[0], row.split(':')[1].split()[1]): [] for row in
              lst_in}
shop_items = {key: [key, key.total] for key in shop_items}
# print(shop_items)
