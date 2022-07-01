class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            last_elem = self.last_element()
            last_elem.next = obj

    def last_element(self, pop=False):
        temp_obj = self.top
        while temp_obj.next is not None:
            if pop:
                if temp_obj.next.next is None:
                    return temp_obj

            temp_obj = temp_obj.next
        else:
            return temp_obj

    def pop_back(self):
        elem = self.last_element(True)
        if self.top.next is None:
            self.top = None
        else:
            elem.next = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for elem in other:
            self.push_back(StackObj(elem))
        return self


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


st = Stack()

obj1 = StackObj('1')
obj2 = StackObj('2')
obj3 = StackObj('3')
#
# st.push_back(obj1)
# st.push_back(obj2)
# st.push_back(obj3)
#
# st.pop_back()
# st.pop_back()
# st.pop_back()
# pass


# добавление нового объекта класса StackObj в конец односвязного списка st
st = st + obj1
st += obj2

# добавление нескольких объектов в конец односвязного списка
st = st * ['data_1', 'data_2', 'data_N']
st *= ['data_1', 'data_2', 'data_N']
pass
