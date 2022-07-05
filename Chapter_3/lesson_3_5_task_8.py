class FileAcceptor:
    def __init__(self, *args):
        self.lst = args

    def __call__(self, filename, *args, **kwargs):
        return True if filename.split('.')[-1] in self.lst else False

    def __add__(self, other):
        return FileAcceptor(*set(self.lst + other.lst))


acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2  # ("jpg", "jpeg", "png", "bmp")

filenames = ["boatjpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
a = filter(acceptor12, filenames)
print(*a)
