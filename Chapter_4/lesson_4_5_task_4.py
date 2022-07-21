class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    __counter = 0

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self._id = self.auto_increment()

    @classmethod
    def auto_increment(cls):
        id = cls.__counter
        cls.__counter += 1
        return id

    def get_id(self):
        return self._id
