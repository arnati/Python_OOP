import sys


class StreamData:
    def create(self, FIELDS, lst_in):
        if len(FIELDS) == len(lst_in):
            for i in range(len(FIELDS)):
                setattr(self, FIELDS[i], lst_in[i])
            else:
                return True
        else:
            return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
