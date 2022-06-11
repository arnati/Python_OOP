class Viber:
    lst_msg = list()

    @classmethod
    def add_message(cls, msg):
        cls.lst_msg.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.lst_msg.remove(msg)

    @classmethod
    def set_like(cls, msg):
        cls.lst_msg[cls.lst_msg.index(msg)].fl_like = True

    @classmethod
    def show_last_message(cls):
        print(*cls.lst_msg[-1])

    @classmethod
    def total_messages(cls):
        return len(cls.lst_msg)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like
