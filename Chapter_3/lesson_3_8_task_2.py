class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.lst = [*self.__dict__.items()]

    def __getitem__(self, item):
        if not isinstance(item, int) or not (0 <= item < len(self.lst)):
            raise IndexError('неверный индекс поля')
        else:
            return self.lst[item][1]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or not (0 <= key < len(self.lst)):
            raise IndexError('неверный индекс поля')
        else:
            self.__dict__[self.lst[key][0]] = value
            self.__dict__.pop('lst')
            self.lst = [*self.__dict__.items()]


r = Record(pk=1, title='Python ООП', author='Балакирев')
r[0] = 2  # доступ к полю pk
r[1] = 'Супер курс по ООП'  # доступ к полю title
r[2] = 'Балакирев С.М.'  # доступ к полю author
print(r[1])  # Супер курс по ООП
r[3]  # генерируется исключение IndexError
