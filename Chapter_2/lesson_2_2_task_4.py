class Car:
    def __init__(self):
        self.__model = str()

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.check_value(model):
            self.__model = model

    @staticmethod
    def check_value(string):
        if type(string) is str:
            if 2 <= len(string) <= 100:
                return True
        return False
