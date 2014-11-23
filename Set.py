class SetClass:
    points = []

    def describe(self, full):
        print "Containing %d points." % len(self.points)

        if full:
            for point in self.points:
                point.describe()

    def add(self, point):
        self.points.append(point)
