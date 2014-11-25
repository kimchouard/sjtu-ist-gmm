class SetClass:
    points = []

    def add(self, point):
        self.points.append(point)

    def getPoint(self, n):
        return self.points[n]

    def getPlotData(self):
        X = []
        Y = []
        pointSize = 5
        C = []

        for point in self.points:
            X.append(point.getDim(0))
            Y.append(point.getDim(1))
            C.append(point.getColor())

        return [X, Y, pointSize, C]

    def describe(self, full):
        print "Containing %d points." % len(self.points)

        if full:
            for point in self.points:
                point.describe()
