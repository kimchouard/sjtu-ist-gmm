class PointClass:
    def __init__(self, dims, label=0):
        """
        Initialize a point from parameters:
            - dims: array containing point values
            !! IMPORTANT respect the form [[x1], [x2], ...]
            - label (falcultative): define to which class label
            the point belongs to
        """
        self.dims = dims
        self.label = label

    def getDim(self, i):
        return self.dims[i]

    def getDims(self):
        return self.dims

    def getLabel(self):
        return self.label

    def getDimNum(self):
        return len(self.dims)

    def getColor(self):
        if self.label == 1:
            return [1, 0, 0]
        elif self.label == 2:
            return [0, 1, 0]
        else:
            return [0, 0, 1]

    def describe(self):
        print "Point %d at (%f, %f)" % (self.label, self.dims[0], self.dims[1])
