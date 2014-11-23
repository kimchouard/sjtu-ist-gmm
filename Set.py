class SetClass:
    points = []

    def add(self, point):
        self.points.append(point)

    def getPlotData(self):
        X = []
        Y = []
        pointSize = 5
        C = []

        for point in self.points:
            X.append(point.getX())
            Y.append(point.getY())
            C.append(point.getColor())

        return [X, Y, pointSize, C]

    def describe(self, full):
        print "Containing %d points." % len(self.points)

        if full:
            for point in self.points:
                point.describe()
