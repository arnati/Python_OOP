class PolyLine:
    def __init__(self, start_coord, *args):
        self.start_coord = start_coord
        self.lst = list(args)
        self.lst.append(self.start_coord)

    def add_coord(self, x, y):
        self.lst.append((x, y))

    def remove_coord(self, indx):
        self.lst.pop(indx)

    def get_coords(self):
        return self.lst
