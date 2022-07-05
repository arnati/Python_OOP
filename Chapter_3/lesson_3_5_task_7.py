class Morph:
    def __init__(self, *args):
        self.lst = args

    def add_word(self, word):
        self.lst += (word,)

    def get_words(self):
        return self.lst

    def __eq__(self, other):
        for x in self.lst:
            if x.lower() in other.lower().split():
                return True
        return False


words = [
    "связь связи связью связей связям связями связях",
    "формула формулы формуле формулу формулой формул формулам формулами формулах",
    "вектор вектора вектору вектором векторе векторы векторов векторам векторами векторах",
    "эффект эффекта эффекту эффектом эффекте эффекты эффектов эффектам эффектами эффектах",
    "день дня дню днем дне дни дням днями днях"
]

dict_words = [Morph(*row.split()) for row in words]

text = ' '.join([word[1:] if word[0] in ('–', '?', '!', ',', '.', ';') else word[0:-1] if word[-1] in (
    '–', '?', '!', ',', '.', ';') else word for word in input().split()])

i = 0
for word in text.split():
    for obj in dict_words:
        if word == obj:
            i += 1

print(i)
