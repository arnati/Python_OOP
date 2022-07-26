class ValidatorString:
    def __init__(self, min_length, max_length, chars=""):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):

        if not isinstance(string, str) or not (self.min_length <= len(string) <= self.max_length):
            raise ValueError('недопустимая строка')

        if self.chars != "":
            for i in self.chars:
                if i in string:
                    break
            else:
                raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request):
        self.check_key(request)
        self.login_validator.is_valid(request['login'])
        self.password_validator.is_valid(request['password'])

        setattr(self, '_login', request['login'])
        setattr(self, '_password', request['password'])

    def check_key(self, request):
        if 'login' not in request or 'password' not in request:
            raise TypeError('в запросе отсутствует логин или пароль')


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
