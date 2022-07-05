class MoneyR:
    def __init__(self, volume=0, cb=None):
        self.__cb = cb
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, rub):
        self.__volume = rub

    def __eq__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        elif isinstance(other, MoneyD):
            return True if CentralBank.dollar_to_rub(other) - 0.1 <= self.volume <= CentralBank.dollar_to_rub(
                other) + 0.1 else False
        elif isinstance(other, MoneyE):
            return True if CentralBank.euro_to_rub(other) - 0.1 <= self.volume <= CentralBank.euro_to_rub(
                other) + 0.1 else False
        elif isinstance(other, MoneyR):
            return True if other.volume - 0.1 <= self.volume <= other.volume + 0.1 else False

    def __lt__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        elif isinstance(other, MoneyD):
            return True if self.volume < CentralBank.dollar_to_rub(other) else False
        elif isinstance(other, MoneyE):
            return True if self.volume < CentralBank.euro_to_rub(other) else False
        elif isinstance(other, MoneyR):
            return True if self.volume < other.volume else False

    def __ge__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        elif isinstance(other, MoneyD):
            return True if self.volume >= CentralBank.dollar_to_rub(other) else False
        elif isinstance(other, MoneyE):
            return True if self.volume >= CentralBank.euro_to_rub(other) else False
        elif isinstance(other, MoneyR):
            return True if self.volume >= other.volume else False


class MoneyD:
    def __init__(self, volume=0, cb=None):
        self.__cb = cb
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, dollar):
        self.__volume = dollar

    def __eq__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        elif isinstance(other, MoneyR):
            return True if other.volume - 0.1 <= CentralBank.dollar_to_rub(self) <= other.volume + 0.1 else False
        elif isinstance(other, MoneyE):
            return True if CentralBank.euro_to_rub(other) - 0.1 <= CentralBank.dollar_to_rub(self) <= CentralBank.euro_to_rub(other) + 0.1 else False
        elif isinstance(other, MoneyD):
            # print(f"{CentralBank.dollar_to_rub(other) - CentralBank.dollar_to_rub(self)/100 * 0.1} <= {CentralBank.dollar_to_rub(self)} <= {CentralBank.dollar_to_rub(other) + CentralBank.dollar_to_rub(self)/100 * 0.1}")
            return True if CentralBank.dollar_to_rub(other) - CentralBank.dollar_to_rub(self)/100 * 0.1 <= CentralBank.dollar_to_rub(self) <= CentralBank.dollar_to_rub(other) + CentralBank.dollar_to_rub(self)/100 * 0.1 else False

    def __lt__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        elif isinstance(other, MoneyR):
            return True if CentralBank.dollar_to_rub(self) < other.volume else False
        elif isinstance(other, MoneyE):
            return True if CentralBank.dollar_to_rub(self) < CentralBank.euro_to_rub(other) else False
        elif isinstance(other, MoneyD):
            return True if CentralBank.dollar_to_rub(self) < CentralBank.dollar_to_rub(other) else False

    def __ge__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        elif isinstance(other, MoneyR):
            return True if CentralBank.dollar_to_rub(self) >= other.volume else False
        elif isinstance(other, MoneyE):
            return True if CentralBank.dollar_to_rub(self) >= CentralBank.euro_to_rub(other) else False
        elif isinstance(other, MoneyD):
            return True if CentralBank.dollar_to_rub(self) >= CentralBank.dollar_to_rub(other) else False


class MoneyE:
    def __init__(self, volume=0, cb=None):
        self.__cb = cb
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, euro):
        self.__volume = euro

    def __eq__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        elif isinstance(other, MoneyR):
            return True if other.volume - 0.1 <= CentralBank.euro_to_rub(self) <= other.volume + 0.1 else False
        elif isinstance(other, MoneyD):
            return True if CentralBank.dollar_to_rub(other) - 0.1 <= CentralBank.euro_to_rub(self) <= CentralBank.dollar_to_rub(other) + 0.1 else False
        elif isinstance(other, MoneyE):
            print(f"{CentralBank.euro_to_rub(other) - CentralBank.euro_to_rub(self)/100 * 0.1} <= {CentralBank.euro_to_rub(self)} <= {CentralBank.euro_to_rub(other) + CentralBank.euro_to_rub(self)/100 * 0.1}")
            return True if CentralBank.euro_to_rub(other) - CentralBank.euro_to_rub(self)/100 * 0.1 <= CentralBank.euro_to_rub(self) <= CentralBank.euro_to_rub(other) + CentralBank.euro_to_rub(self)/100 * 0.1 else False

    def __lt__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        elif isinstance(other, MoneyR):
            return True if CentralBank.euro_to_rub(self) < other.volume else False
        elif isinstance(other, MoneyD):
            return True if CentralBank.euro_to_rub(self) < CentralBank.dollar_to_rub(other) else False
        elif isinstance(other, MoneyE):
            return True if CentralBank.euro_to_rub(self) < CentralBank.euro_to_rub(other) else False

    def __ge__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        elif isinstance(other, MoneyR):
            return True if CentralBank.euro_to_rub(self) >= other.volume else False
        elif isinstance(other, MoneyD):
            return True if CentralBank.euro_to_rub(self) >= CentralBank.dollar_to_rub(other) else False
        elif isinstance(other, MoneyE):
            return True if CentralBank.euro_to_rub(self) >= CentralBank.euro_to_rub(other) else False


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls

    @classmethod
    def dollar_to_rub(cls, obj):
        return obj.volume * cls.rates['rub']

    @classmethod
    def euro_to_rub(cls, obj):
        return obj.volume * cls.rates['rub'] * cls.rates['euro']


# r = MoneyR(45000)
# d = MoneyD(500)
#
#
# CentralBank.register(r)
# CentralBank.register(d)
#
#
# if r > d:
#     print("неплохо")
# else:
#     print("нужно поднажать")


d1 = MoneyE(100.0000001)
d2 = MoneyE(100)

CentralBank.register(d1)
CentralBank.register(d2)

print(d1 == d2)