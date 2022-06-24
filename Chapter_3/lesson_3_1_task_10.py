import time


class GeyserClassic:
    MAX_DATE_FILTER = 100
    filter_dict = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num, filter):
        if self.check_value(slot_num, filter):
            self.filter_dict[slot_num] = filter

    def check_value(self, slot_num, filter):
        if self.filter_dict[slot_num] is None:
            if slot_num == 1 and isinstance(filter, Mechanical):
                return True
            elif slot_num == 2 and isinstance(filter, Aragon):
                return True
            elif slot_num == 3 and isinstance(filter, Calcium):
                return True
        return False

    def remove_filter(self, slot_num):
        self.filter_dict[slot_num] = None

    def get_filters(self):
        return tuple(self.filter_dict.values())

    def water_on(self):
        if None not in self.get_filters():
            for obj in self.get_filters():
                if not (0 <= (time.time() - obj.date) <= self.MAX_DATE_FILTER):
                    return False
            else:
                return True
        return False


class Mechanical:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, x):
        self.__date = x

    def __setattr__(self, key, value):
        if key != "date":
            object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, x):
        self.__date = x

    def __setattr__(self, key, value):
        if key != "date":
            object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, x):
        self.__date = x

    def __setattr__(self, key, value):
        if key != "date":
            object.__setattr__(self, key, value)


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()  # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
