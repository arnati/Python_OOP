class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, key, value):
        if key == "_model" and not isinstance(value, str):
            raise TypeError('неверный тип аргумента')
        elif key in ("_mass", "_speed", "_top"):
            if type(value) not in (int, float) or value < 0:
                raise TypeError('неверный тип аргумента')
        object.__setattr__(self, key, value)


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self.check_value(chairs)
        self._chairs = chairs

    @staticmethod
    def check_value(chairs):
        if type(chairs) is not int or chairs < 0:
            raise TypeError('неверный тип аргумента')


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self.check_value(weapons)
        self._weapons = weapons

    @staticmethod
    def check_value(weapons):
        if not isinstance(weapons, dict):
            raise TypeError('неверный тип аргумента')


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
