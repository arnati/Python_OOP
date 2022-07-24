lst_in = input().split()


def check_int(value):
    try:
        return True if int(value) else False
    except:
        return False


print(sum(map(int, filter(check_int, lst_in))))
