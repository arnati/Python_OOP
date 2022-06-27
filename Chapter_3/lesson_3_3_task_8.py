class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        if self.__len__():
            return f"{str(self.clock1.hours - self.clock2.hours).rjust(2, '0')}: " \
                   f"{str(self.clock1.minutes - self.clock2.minutes).rjust(2, '0')}:" \
                   f" {str(self.clock1.seconds - self.clock2.seconds).rjust(2, '0')}"
        else:
            return "00: 00: 00"

    def __len__(self):
        l = Clock.get_time(self.clock1) - Clock.get_time(self.clock2)
        return 0 if l < 0 else l


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


dt = DeltaClock(Clock(2, 45, 0), Clock(3, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
