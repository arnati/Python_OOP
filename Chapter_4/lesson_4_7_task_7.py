class Note:
    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == "_name":
            if value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
                raise ValueError('недопустимое значение аргумента')
        elif key == "_ton":
            if type(value) is not int or value not in (-1, 0, 1):
                raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, key, value)


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
    __obj = None

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self):
        for i in range(len(self.__slots__)):
            setattr(self, self.__slots__[i], Note(self.notes[i], 0))

    def __getitem__(self, item):
        self.check_index(item)
        return getattr(self, self.__slots__[item])

    def check_index(self, index):
        if type(index) is not int or not (0 <= index < len(self.__slots__)):
            raise IndexError('недопустимый индекс')


notes = Notes()

nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1  # изменение тональности ноты фа

pass
