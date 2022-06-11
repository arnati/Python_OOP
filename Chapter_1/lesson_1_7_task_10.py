class AppStore:
    lst_app = list()

    def add_application(self, app):
        self.lst_app.append(app)

    def remove_application(self, app):
        self.lst_app.remove(app)

    def block_application(self, app):
        self.lst_app[self.lst_app.index(app)].blocked = True

    def total_apps(self):
        return len(self.lst_app)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked



