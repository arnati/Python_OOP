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
        if self.check_obj(next):
            self.__next = next

    @classmethod
    def check_obj(cls, obj):
        if type(obj) is StackObj or obj is None:
            return True
        return False


class Stack:
    def __init__(self):
        self.top = None

    @staticmethod
    def lost_obj_in_stack(obj, pop=False):
        lost_obj = obj
        new_lost_obj = obj
        while True:
            if lost_obj.next is None:
                if pop:
                    return lost_obj, new_lost_obj
                else:
                    return lost_obj
            else:
                if lost_obj != new_lost_obj:
                    new_lost_obj = lost_obj

                lost_obj = lost_obj.next

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            lost_obj = self.lost_obj_in_stack(self.top)
            lost_obj.next = obj

    def pop(self):
        lost_obj = self.lost_obj_in_stack(self.top, True)

        if lost_obj[0] == lost_obj[1]:
            self.top = None
            return self.top
        else:
            lost_obj[1].next = None

        return lost_obj[0]

    def get_data(self):
        flag = True
        obj = self.top
        lst = list()

        while flag:
            if obj is None:
                break

            if obj.next is None:
                lst.append(obj.data)
                flag = False
            else:
                lst.append(obj.data)
                obj = obj.next

        return lst


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
st.pop()
st.pop()
res = st.get_data()  # ['obj1', 'obj2']

print(res)
