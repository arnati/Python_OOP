class ObjList:
    lst_id = list()

    def __new__(cls, *args, **kwargs):
        cls.lst_id.append(super().__new__(cls))
        return cls.lst_id[-1]

    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None and self.tail is None:
            self.head = self.tail = obj
        else:
            current_obj = self.tail
            self.tail = obj
            self.tail.prev = current_obj
            current_obj.next = obj

    def remove_obj(self, indx):
        if indx == 0:
            if self.__len__() == 1:
                self.head = self.tail = None
            else:
                self.head = ObjList.lst_id[1]
                self.head.prev = None
                ObjList.lst_id.pop(0)
        elif indx == self.__len__() - 1:
            if self.__len__() == 1:
                self.head = self.tail = None
            else:
                self.tail = ObjList.lst_id[-2]
                self.tail.next = None
                ObjList.lst_id.pop(-1)
        else:
            ObjList.lst_id[indx - 1].next = ObjList.lst_id[indx].next
            ObjList.lst_id[indx + 1].prev = ObjList.lst_id[indx].prev

    def __len__(self):
        return len(ObjList.lst_id)

    def linked_lst(self, indx):
        return ObjList.lst_id[indx].data

    def __call__(self, *args, **kwargs):
        return self.linked_lst(args[0])


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(1)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1)  # s = Balakirev
