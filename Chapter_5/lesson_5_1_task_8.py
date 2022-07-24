lst_in = input().split()


def check_type(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return value


lst_out = list(map(check_type, lst_in))
