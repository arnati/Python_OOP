class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        print(*(i for i in self.data if Graph.LIMIT_Y[0] <= i <= Graph.LIMIT_Y[-1]))


lst = [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]

graph_1 = Graph()
graph_1.set_data(lst)
graph_1.draw()
