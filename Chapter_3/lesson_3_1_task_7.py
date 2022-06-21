class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = list()

    def add_app(self, app):
        if app.__class__.count < 2:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    count = 0

    def __new__(cls, *args, **kwargs):
        cls.count += 1
        return super().__new__(cls)

    def __init__(self):
        self.name = "ВКонтакте"

    @classmethod
    def __del__(cls):
        cls.count -= 1


class AppYouTube:
    count = 0

    def __new__(cls, *args, **kwargs):
        cls.count += 1
        return super().__new__(cls)

    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max

    @classmethod
    def __del__(cls):
        cls.count -= 1


class AppPhone:
    count = 0

    def __new__(cls, *args, **kwargs):
        cls.count += 1
        return super().__new__(cls)

    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list

    @classmethod
    def __del__(cls):
        cls.count -= 1


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
