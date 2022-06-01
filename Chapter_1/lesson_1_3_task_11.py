class Translator:
    dict_word = dict()

    def add(self, eng, rus):
        if eng.lower() in Translator.dict_word.keys():
            Translator.dict_word[eng.lower()] = [*Translator.dict_word[eng.lower()], rus]
        else:
            Translator.dict_word.setdefault(eng, [rus])

    def remove(self, eng):
        Translator.dict_word.pop(eng)

    def translate(self, eng):
        return Translator.dict_word.get(eng)


tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove("car")

print(*tr.translate("go"))
