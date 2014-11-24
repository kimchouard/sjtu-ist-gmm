class PointClass:
    def __init__(self, d1, d2, label=0):
        self.dims = [d1, d2]
        self.label = label

    def getX(self):
        return self.dims[0]

    def getY(self):
        return self.dims[1]

    def getLabel(self):
        return self.label

    def getColor(self):
        if self.label == 1:
            return [1, 0, 0]
        elif self.label == 2:
            return [0, 1, 0]
        else:
            return [0, 0, 1]

    def describe(self):
        print "Point %d at (%f, %f)" % (self.label, self.dims[0], self.dims[1])
