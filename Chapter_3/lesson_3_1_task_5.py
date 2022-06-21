class Course:
    def __init__(self, name):
        self.name = name
        self.modules = list()

    def add_module(self, lesson):
        self.modules.append(lesson)

    def remove_module(self, indx):
        self.modules.pop(indx)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = list()

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class LessonItem:
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == "title":
            if type(value) is not str:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)
        elif key in ("practices", "duration"):
            if type(value) is not int or value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)

    def __getattr__(self, item):
        if item not in self.__dict__.keys():
            return False

    def __delattr__(self, item):
        if item in (self.__dict__.keys()):
            raise AttributeError(f"Атрибуты {self.__dict__.keys()} удалять запрещено.")
        object.__delattr__(self, item)


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
