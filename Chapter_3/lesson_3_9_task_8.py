class Stack:
    def __init__(self):
        self.top = None
        self.counter = 0

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            lost_obj = self.lost_obj()
            lost_obj.next = obj
        self.counter += 1

    def push_front(self, obj):
        next_obj = self.top
        self.top = obj
        self.top.next = next_obj
        self.counter += 1

    def lost_obj(self):
        current_obj = self.top

        while current_obj.next is not None:
            current_obj = current_obj.next
        return current_obj

    def __getitem__(self, item):
        self.check_index(item)
        i = 0
        current_obj = self.top
        while current_obj.next is not None:
            if i == item:
                return current_obj.data
            current_obj = current_obj.next
        else:
            return current_obj.data

    def __setitem__(self, key, value):
        self.check_index(key)
        i = 0
        current_obj = self.top
        while current_obj.next is not None:
            if i == key:
                current_obj.data = value
                break
            current_obj = current_obj.next
        else:
            current_obj.data = value

    def check_index(self, index):
        if not (isinstance(index, int)) or not (0 <= index < self.counter):
            raise IndexError('неверный индекс')

    def __len__(self):
        return self.counter

    def __iter__(self):
        current_obj = self.top
        while current_obj.next is not None:
            yield current_obj
            current_obj = current_obj.next
        else:
            yield current_obj


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


s = Stack()

obj1 = StackObj(1)
obj2 = StackObj(2)
obj3 = StackObj(3)

s.push_back(obj1)
s.push_back(obj2)
s.push_back(obj3)

obj4 = StackObj(-1)
obj5 = StackObj(-2)
obj6 = StackObj(-3)

s.push_front(obj4)
s.push_front(obj5)
s.push_front(obj6)

# print(s[0])
s[0] = 11111
# print(s[0])

# print(s[5])


for obj in s: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль
