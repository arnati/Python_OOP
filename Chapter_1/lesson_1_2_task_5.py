class Car:
    model = ""
    color = ""
    number = ""


setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Розовый")
setattr(Car, 'number', "О111АА77")

print(Car.__dict__['color'])
