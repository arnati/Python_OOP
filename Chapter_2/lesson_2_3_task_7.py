class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.__min_length = min_length
        self.__max_length = max_length

    def validate(self, string):
        if type(string) is str and self.__min_length <= len(string) <= self.__max_length:
            return True
        return False


class StringValue:
    def __init__(self, validator=ValidateString()):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue()
    password = StringValue()
    email = StringValue()

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return list(self.__dict__.values())

    def show(self):
        print(f"<form> \nЛогин: {self.login} \nПароль: {self.password} \nEmail: {self.email} \n</form>")


form = RegisterForm('логин', 'пароль', 'email')
# form.show()
print(form.get_fields())
