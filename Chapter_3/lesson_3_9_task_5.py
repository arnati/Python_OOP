class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.__dict__.update({'fio': fio, 'job': job, 'old': old, 'salary': salary, 'year_job': year_job})
        self.current_index = 0

    def __getitem__(self, item):
        self.check_index(item)
        key = list(self.__dict__.keys())[item]
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.check_index(key)
        dict_key = list(self.__dict__.keys())[key]
        self.__dict__[dict_key] = value

    def check_index(self, index):
        if not (isinstance(index, int)) or not (0 <= index < len(self.__dict__) - 1):
            raise IndexError('неверный индекс')

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.__dict__) - 1:
            self.current_index += 1
            key = list(self.__dict__.keys())[self.current_index - 1]
            return self.__dict__[key]
        else:
            raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# print(pers[5])
# pers[0] = 'Балакирев С.М.'
# print(pers[0])
for v in pers:
    print(v)
# pers[4] = 123  # IndexError
