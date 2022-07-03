class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.lst = list()

    def add_track(self, tr):
        self.lst.append(tr)

    def get_tracks(self):
        return self.lst

    def __len__(self):
        l = 0
        for i in range(len(self.lst)):
            if l == 0:
                x = self.lst[i].to_x - self.start_x
                y = self.lst[i].to_y - self.start_y
            else:
                x = self.lst[i].to_x - self.lst[i - 1].to_x
                y = self.lst[i].to_y - self.lst[i - 1].to_y

            l += (x ** 2 + y ** 2) ** 0.5
        else:
            return int(l)

    def __eq__(self, other):
        return True if self.__len__() == other.__len__() else False

    def __lt__(self, other):
        return True if self.__len__() < other.__len__() else False


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1 = Track(0, 0)
track2 = Track(0, 1)

track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
