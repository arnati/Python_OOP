class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        res = self.func()
        lst = list()

        for i in res.split():
            if '-' in i:
                if i.replace('-', '', 1).isdigit():
                    lst.append(int(i))
                else:
                    break
            elif i.isdigit():
                lst.append(int(i))
            else:
                break
        else:
            return lst


@InputDigits
def input_dg():
    return input()


res = input_dg()

print(res)
