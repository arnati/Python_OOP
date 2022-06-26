class InputValues:
    def __init__(self, render):  # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return self.render(func)

        return wrapper


class RenderDigit:
    def __call__(self, *args, **kwargs):
        # res = link() if link is not None else args[0]
        res = args[0]() if type(args[0]) not in (int, float, str, bool) else args[0]

        lst = list()

        for i in res.split():
            if '-' in i:
                if i.replace('-', '', 1).isdigit():
                    lst.append(int(i))
                else:
                    lst.append(None)
            elif i.isdigit():
                lst.append(int(i))
            else:
                lst.append(None)
        else:
            return lst if type(args[0]) not in (int, float, str, bool) else lst[0]


render = RenderDigit()

# d1 = render("123")  # 123 (целое число)
# d2 = render("45.54")  # None (не целое число)
# d3 = render("-56")  # -56 (целое число)
# d4 = render("12fg")  # None (не целое число)
# d5 = render("abc")  # None (не целое число)


@InputValues(render=render)
def input_dg():
    return input()


res = input_dg()

print(res)
