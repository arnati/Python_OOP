class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    def __call__(self, *args, **kwargs):
        if self.type_list == "ol":
            s = f"<{self.type_list}>\n"
        else:
            s = f"<ul>\n"

        for i in args[0]:
            s += f"<li>{i}</li>\n"
        else:
            if self.type_list == "ol":
                s += f"</{self.type_list}>\n"
            else:
                s += f"</ul>\n"
            return s


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)

print(html)
