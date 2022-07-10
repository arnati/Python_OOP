class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.lst = list()

    def add_point(self, x, y, speed):
        self.lst.append([x, y, speed])

    def __getitem__(self, item):
        if not isinstance(item, int) or not (0 <= item < len(self.lst)):
            raise IndexError('некорректный индекс')
        return tuple(self.lst[item][:2]), self.lst[item][2]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or not (0 <= key < len(self.lst)):
            raise IndexError('некорректный индекс')
        self.lst[key][2] = value


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError
