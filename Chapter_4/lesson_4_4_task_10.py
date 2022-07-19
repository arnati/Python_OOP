CURRENT_OS = 'windows'  # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory:
    obj = None

    def __new__(cls, title, path, exts, *args, **kwargs):
        if CURRENT_OS == 'windows':
            cls.obj = cls.create_windows_filedialog(title, path, exts)
        elif CURRENT_OS == 'linux':
            cls.obj = cls.create_linux_filedialog(title, path, exts)
        return cls.obj

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)


a = FileDialogFactory('1', '2', '3')
pass
