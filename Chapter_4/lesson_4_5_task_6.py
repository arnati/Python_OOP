from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    __counter = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.auto_increment()

    @classmethod
    def auto_increment(cls):
        id = cls.__counter
        cls.__counter += 1
        return id

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
print(form.get_pk())
