def check_type(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return value


a, b = map(check_type, input().split())

try:
    print(a + b)
except TypeError:
    print(str(a) + str(b))



