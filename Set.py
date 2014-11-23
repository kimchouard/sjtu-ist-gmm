class SetClass:
    points = []

    def describe(self):
        for point in self.points:
            point.describe()

    def add(self, point):
        self.points.append(point)
