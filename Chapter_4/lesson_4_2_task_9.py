class IteratorAttrs:
    def __iter__(self):
        for k, v in self.__dict__.items():
            yield k, v


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory



phone = SmartPhone('model', 'size', 'memory')
for attr, value in phone:
    print(attr, value)
