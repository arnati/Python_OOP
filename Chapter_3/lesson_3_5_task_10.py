class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    @staticmethod
    def mass(obj):
        return obj.ro * obj.volume

    def __eq__(self, other):
        if type(other) in (int, float):
            return True if self.mass(self) == other else False
        else:
            return True if self.mass(self) == self.mass(other) else False

    def __lt__(self, other):
        if type(other) in (int, float):
            return True if self.mass(self) < other else False
        else:
            return True if self.mass(self) < self.mass(other) else False
