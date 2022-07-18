class SoftList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.max_index = len(*args)

    def __getitem__(self, item):
        if -1 <= item < self.max_index:
            return super().__getitem__(item)
        return False

    def __setitem__(self, key, value):
        if isinstance(key, int) and -1 <= key < self.max_index:
            super().__setitem__(key, value)
        return False


lst = SoftList("python")
print(lst[0])
print(lst[-1])

# lst[0] = 1111
lst[-1] = 'AAAAAAAAAAAAAAAAAAAAA'

print(lst[0])
print(lst[-1])