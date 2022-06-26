class Model:
    def __init__(self):
        self.lst = dict()

    def query(self, **kwargs):
        self.lst = kwargs

    def __str__(self):
        if len(self.lst) == 0:
            return "Model"
        else:
            s = "Model: "
            for key, value in self.lst.items():
                s += f"{key} = {value}, "
            return s[:-2]


model = Model()
# model.query(id=1, fio='Sergey', old=33)
print(model)
