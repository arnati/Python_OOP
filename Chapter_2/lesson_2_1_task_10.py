import string
import random

# random.seed(1)


class EmailValidator:
    available_chars = string.ascii_letters + string.digits + '@._'

    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def __is_email_str(email):
        if type(email) is str:
            return True
        return False

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            flag = False
            for i in email:
                if i not in cls.available_chars:
                    return False

                if i == '.' and flag is False:
                    flag = True
                elif i == '.' and flag:
                    return False
                else:
                    flag = False
            else:
                if len(email) > 100:
                    return False

                if email.count("@") != 1:
                    return False
                elif len(email) - email.index("@") - 1 > 50:
                    return False

                if email.count(".", email.index("@"), len(email)) == 0:
                    return False

            return True

    @classmethod
    def get_random_email(cls):
        return ''.join(random.sample(cls.available_chars, random.randint(0, 50))) + '@gmail.com'

# class TestClass:
#     def test_check_email_1(self):
#         """
#         Тест на допустимые символы: латинский алфавит, цифры, символы
#         подчеркивания, точки и собачка @
#         """
#         email = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@._"
#         assert EmailValidator.check_email(email) is True
#
#     def test_check_email_2(self):
#         """
#         Не должно быть двух точек подряд
#         """
#         email = "absd..bsd"
#         assert EmailValidator.check_email(email) is False
#
#     def test_check_email_3(self):
#         """
#         длина email до символа @ не должна превышать 100 (сто включительно)
#         """
#         email = "a" * 101
#         assert EmailValidator.check_email(email) is False
#
#     def test_check_email_4(self):
#         """
#         длина email после символа @ не должна быть больше 50 (включительно)
#         """
#         email = "a@." + "r" * 49
#         assert EmailValidator.check_email(email) is True

# email = "a@" + "r" * 51
# EmailValidator.check_email(email)


print(EmailValidator.get_random_email())