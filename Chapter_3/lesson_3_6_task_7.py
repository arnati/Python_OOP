import sys


class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = dict()

    def write(self, record):
        if len(self.dict_db) == 0:
            self.dict_db[record] = [record]
        else:
            dict_db_copy = dict.copy(self.dict_db)
            for key in self.dict_db.keys():
                if key == record:
                    dict_db_copy[key].append(record)
                    break
            else:
                dict_db_copy[record] = [record]
            self.dict_db = dict_db_copy

    def read(self, pk):
        for value in self.dict_db.values():
            for obj in value:
                if obj.pk == pk:
                    return obj


class Record:
    __increment = 0

    @classmethod
    def auto_increment(cls):
        temp = cls.__increment
        cls.__increment += 1
        return temp

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self.auto_increment()

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


# lst_in = [
#     'Балакирев С.М.; программист; 33',
#     'Кузнецов А.В.; разведчик-нелегал; 35',
#     'Кузнецов А.В.; разведчик-нелегал2; 35',
#     'Кузнецов А.В.; разведчик-нелегал; 35',
#     'Суворов А.В.; полководец; 42',
#     'Иванов И.И.; фигурант всех подобных списков; 26',
#     'Балакирев С.М.; преподаватель; 33'
# ]
lst_in = list(map(str.strip, sys.stdin.readlines()))

db = DataBase("хз")
for row in lst_in:
    fio, descr, old = row.split('; ')
    db.write(Record(fio, descr, old))
