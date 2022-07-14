class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.min_len_row = 1
        for row in self.lst:
            if len(row) < self.min_len_row:
                raise IndexError('index out of range')
            for element in range(self.min_len_row):
                yield row[element]
            self.min_len_row += 1


lst = [['1', '!', '!'],
       ['2', 9],
       ['4', '5', '6', '!', '!'],
       ['7', '8', '9', '10']]

it = TriangleListIterator(lst)
print(type(it))

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)
it_iter = iter(it)
x = next(it_iter)
y = next(it_iter)
print(x)
print(y)

# print([i for i in it])

# ls = [['1'], [2, 3], [4, 5, 6], ['7', 8, '9', 10]]
# ls_one = [x for row in ls for x in row]
# print(ls_one)
