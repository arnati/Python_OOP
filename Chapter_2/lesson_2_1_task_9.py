class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None and self.tail is None:
            self.head = obj
            self.tail = obj
        else:
            current_obj = self.tail
            self.tail = obj
            current_obj.set_next(obj)
            self.tail.set_prev(current_obj)

    def remove_obj(self):
        self.tail = self.tail.get_prev()

    def get_data(self):
        temp_obj = self.head
        lst = list()

        while temp_obj != None:
            lst.append(temp_obj.get_data())
            temp_obj = temp_obj.get_next()
        else:
            return lst


class ObjList:
    # num_obj = 0
    #
    # def __new__(cls, *args, **kwargs):
    #     cls.num_obj += 1
    #     return super().__new__(cls)
    #
    # def __del__(self):
    #     self.num_obj -= 1

    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']

print(res)
