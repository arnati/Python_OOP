from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if self._top is None:
            self._top = obj
        else:
            last_obj = self.last_obj()
            last_obj._next = obj

    def pop_back(self):
        if self._top._next is None:
            temp_obj = self._top
            self._top = None
            return temp_obj
        elif self._top is None:
            return None
        else:
            pre_last_obj = self.last_obj(True)
            temp_obj = pre_last_obj._next
            pre_last_obj._next = None
            return temp_obj

    def last_obj(self, pop=False):
        current_obj = self._top
        while current_obj._next is not None:
            if pop and current_obj._next._next is None:
                return current_obj

            current_obj = current_obj._next
        return current_obj


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None


st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back()  # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
