def input_int_numbers():
    t = tuple()
    for i in input().split():
        try:
            t += (int(i)),
        except:
            raise TypeError('все числа должны быть целыми')
    return t


while True:
    try:
        print(input_int_numbers())
        break
    except:
        continue
