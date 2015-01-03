import numpy as np

class SetClass:
    points = []

    def add(self, point):
        self.points.append(point)

    def getPoints(self):
        data = []

        for p in self.points:
            data.append(p.getDims())

        return data

    def getPoint(self, n):
        return self.points[n]

    def getLength(self):
        return len(self.points)

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
