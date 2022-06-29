class NewList:
    def __init__(self, *args):
        if len(args) == 0:
            self.lst = list()
        else:
            self.lst = args[0]

    def __sub__(self, other):
        temp = [str(i) for i in self.lst]

        if isinstance(other, NewList):
            for i in other.lst:
                if str(i) in temp:
                    temp.remove(str(i))
        else:
            for i in other:
                if str(i) in temp:
                    temp.remove(str(i))

        lst = list()

        for i in temp:
            if i in ('False', 'True') or i.isalpha():
                if i == 'True':
                    lst.append(True)
                elif i == 'False':
                    lst.append(False)
                else:
                    lst.append(i)
            else:
                if '.' in i:
                    lst.append(float(i))
                else:
                    lst.append(int(i))

        return NewList(lst)

    def __rsub__(self, other):
        return NewList(other) - self

    def get_list(self):
        return self.lst

    def __isub__(self, other):
        temp = [str(i) for i in self.lst]

        if isinstance(other, NewList):
            for i in other.lst:
                if str(i) in temp:
                    temp.remove(str(i))
        else:
            for i in other:
                if str(i) in temp:
                    temp.remove(str(i))

        lst = list()

        for i in temp:
            if i in ('False', 'True') or i.isalpha():
                if i == 'True':
                    lst.append(True)
                elif i == 'False':
                    lst.append(False)
                else:
                    lst.append(i)
            else:
                if '.' in i:
                    lst.append(float(i))
                else:
                    lst.append(int(i))
        self.lst = lst
        return self


lst = NewList()  # пустой список
lst = NewList([-1, 0, 7.56, True])  # список с начальными значениями

lst1 = NewList(['h', 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]

print(res_1.get_list())
