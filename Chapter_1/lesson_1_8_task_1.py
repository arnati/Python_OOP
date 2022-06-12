class Server:
    ip_num = 0

    def __new__(cls, *args, **kwargs):
        cls.ip_num += 1
        return super().__new__(cls)

    def __init__(self):
        self.ip = self.ip_num
        self.buffer = list()

    @staticmethod
    def send_data(data):
        Router.buffer.append(data)

    def get_data(self):
        lst_temp = list(self.buffer)
        self.buffer.clear()
        return lst_temp

    def get_ip(self):
        return self.ip


class Router:
    buffer = list()
    lst_servers = dict()

    @classmethod
    def link(cls, server):
        cls.lst_servers.setdefault(server.get_ip(), server)

    @classmethod
    def unlink(cls, server):
        cls.lst_servers.pop(server.get_ip())

    @classmethod
    def send_data(cls):
        for obj in cls.buffer:
            # cls.lst_servers[obj.ip].buffer.append(obj.data)
            server = cls.lst_servers[obj.ip]
            server.buffer.append(obj)
        else:
            cls.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
router.link(sv_from)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(msg_lst_to[0].data)
print(msg_lst_from[0].data)
