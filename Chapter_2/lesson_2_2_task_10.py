class PhoneBook:
    def __init__(self):
        self.lst_phone = list()

    def add_phone(self, phone):
        self.lst_phone.append(phone)

    def remove_phone(self, indx):
        self.lst_phone.pop(indx)

    def get_phone_list(self):
        return self.lst_phone


class PhoneNumber:
    def __init__(self, number, fio):
        if self.check_value(number, fio):
            self.number = number
            self.fio = fio

    @classmethod
    def check_value(cls, number, fio):
        if type(number) is int and type(fio) is str:
            if len(str(number)) == 11:
                return True
        return False


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()