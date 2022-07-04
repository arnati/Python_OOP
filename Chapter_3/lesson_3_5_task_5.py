class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __gt__(self, other):
        return True if len(self.lst_words) > len(other.lst_words) else False

    def __le__(self, other):
        return True if len(self.lst_words) <= len(other.lst_words) else False


stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

stich = [[word[1:] if word[0] in ('–', '?', '!', ',', '.', ';') else word[0:-1] if word[-1] in (
    '–', '?', '!', ',', '.', ';') else word for word in row.split()] for row in stich]

lst_text = [StringText(row) for row in stich]
lst_text_sorted = sorted(lst_text, key=lambda row: len(row.lst_words), reverse=True)
lst_text_sorted = [' '.join(i.lst_words) for i in lst_text_sorted]


print(lst_text)
# print(*lst_text_sorted[0].lst_words)
print(lst_text_sorted)