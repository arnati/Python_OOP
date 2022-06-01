class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    def add_video(self, video):
        self.videos.append(video)

    def play(self, video_indx):
        v = self.videos[video_indx]
        v.play()


v1 = Video()
v2 = Video()

v1.create("Python")
v2.create("Python ООП")

y = YouTube()
y.add_video(v1)
y.add_video(v2)

y.play(0)
y.play(1)
