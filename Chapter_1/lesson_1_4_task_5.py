'''
class Testfunc:
    def test_1(self):
        tr = TriangleChecker(1, 4, 0)
        assert tr.is_triangle() == 1, "1"

    def test_1_1(self):
        tr = TriangleChecker(1, 4, 0)
        assert tr.is_triangle() == 1, "1"

    def test_2(self):
        tr = TriangleChecker(1, 14, 1)
        assert tr.is_triangle() == 2, "2"

    def test_3(self):
        tr = TriangleChecker(1, 2, 2)
        assert tr.is_triangle() == 3, "3"
'''


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.lst = [a, b, c]

    def is_triangle(self):
        for i in self.lst:
            if isinstance(i, str) or i <= 0:
                return 1
        else:
            if (self.b + self.c) < self.a or (self.a + self.c) < self.b or (self.a + self.b) < self.c:
                return 2
            else:
                return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
