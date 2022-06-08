TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:

    def __new__(cls, *args, **kwargs):
        # print(f'конструируем: {args} | {kwargs}')
        if TYPE_OS == 1:
            instance = super().__new__(DialogWindows)
            instance.name = args[0]
            return instance
        else:
            instance = super().__new__(DialogLinux)
            instance.name = args[0]
            return instance

    def __init__(self, name):
        # print("__init__")
        self.name = name


# d2 = Dialog('test1')
# print(type(d2))
# print(d2.name)
# print(d2.name_class)



