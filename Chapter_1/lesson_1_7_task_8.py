from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        x = digits
        num_card = [x, x, x, x, '-', x, x, x, x, '-', x, x, x, x, '-', x, x, x, x]

        for i, value in enumerate(number):
            if value not in num_card[i]:
                return False
        else:
            return True

    @classmethod
    def check_name(cls, name):
        if len(name.split()) == 2:
            for i in name.replace(' ', ''):
                if i not in cls.CHARS_FOR_NAME:
                    break
            else:
                return True
        return False


# is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# is_name = CardCheck.check_name("SERGEI BALAKIREV$")
