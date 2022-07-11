class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.counter = 0

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            lost_obj = self.lost_elem()
            lost_obj.next = obj

        self.counter += 1

    def pop(self):
        new_lost_obj = self.lost_elem(True)
        self.counter -= 1

        if type(new_lost_obj) is tuple:
            new_lost_obj[0].next = None
            return new_lost_obj[1]
        else:
            self.top = None
            return new_lost_obj

    def lost_elem(self, pop=False):
        current_obj = self.top

        while current_obj.next is not None:
            if pop and current_obj.next.next is None:
                return current_obj, current_obj.next

            current_obj = current_obj.next
        else:
            return current_obj

    def __getitem__(self, item):
        if not isinstance(item, int) or not (0 <= item < self.counter):
            raise IndexError('некорректный индекс')

        if self.counter == 1:
            return self.top

        id = 0
        current_obj = self.top
        while current_obj.next is not None:
            if id == item:
                return current_obj
            current_obj = current_obj.next
            id += 1
        else:
            return current_obj

    def __setitem__(self, key, value):
        if not isinstance(key, int) or not (0 <= key < self.counter):
            raise IndexError('некорректный индекс')

        if key == 0:
            link_to_next_object = self.__getitem__(0)
            value.next = link_to_next_object
            self.top = value
        elif key == self.counter - 1:
            link_to_previous_object = self.__getitem__(key - 1)
            link_to_next_object = None

            link_to_previous_object.next = value
            value.next = link_to_next_object
        else:
            link_to_previous_object = self.__getitem__(key - 1)
            link_to_next_object = self.__getitem__(key).next

            link_to_previous_object.next = value
            value.next = link_to_next_object


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
# res = st[3] # исключение IndexError

pass
