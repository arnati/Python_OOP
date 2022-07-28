class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if len(kwargs) == 0:
            self.e = "Первичный ключ должен быть целым неотрицательным числом"
        elif "id" in kwargs:
            self.e = f"Значение первичного ключа id = {kwargs['id']} недопустимо"
        elif "pk" in kwargs:
            self.e = f"Значение первичного ключа pk = {kwargs['pk']} недопустимо"

    def __str__(self):
        return self.e


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)
