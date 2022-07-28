class DateError(Exception):
    pass


class DateString:
    def __init__(self, date_string):
        self.check_date(date_string)

    def check_date(self, date_string):
        try:
            d, m, y = map(int, date_string.split('.'))
            if not (1 <= d <= 31):
                raise DateError
            if not (1 <= m <= 12):
                raise DateError
            if not (1 <= y <= 3000):
                raise DateError
        except:
            raise DateError
        else:
            date = str(d).rjust(2, '0') + '.' + str(m).rjust(2, '0') + '.' + str(y).rjust(4, '0')
            setattr(self, "date_string", date)

    def __str__(self):
        return self.date_string


try:
    date_string = input()
    d = DateString(date_string)
    print(d)
except:
    print("Неверный формат даты")
