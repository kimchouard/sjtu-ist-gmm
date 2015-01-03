import numpy as np

class SetClass:
    points = []

    def __init__(self):
        """Initialize dict containing data

        WARNING: Need to format after adding all the points"""
        self.dataDic = dict()

    def add(self, dims, label):
        """
        Adding a point, with its dimensions and label.

        WARNING: Need to format after adding all the points
        :param dims:
        :param label:
        :return:
        """
        if(label in self.dataDic.keys()):
            self.dataDic[label].append(dims)
        else:
            self.dataDic[label] = [dims]

    def format(self):
        for label in self.dataDic:
            self.dataDic[label] = np.array(self.dataDic[label])

    def getFeatures(self, label):
        return self.dataDic[label]

    def getPoint(self, label, n):
        return self.dataDic[label][n]

    def getLength(self, label):
        return len(self.dataDic[label])

    def describe(self, full):
        for label in self.dataDic:
            print "Containing %d points." % len(self.dataDic[label])
            if full:
                for point in self.dataDic[label]:
                    print "1,"+str(point)

    # TODO bugfix this function
    # def getPlotData(self):
    #     X = []
    #     Y = []
    #     pointSize = 5
    #     C = []
    #
    #     for label in self.dataDic:
    #         for point in self.points:
    #             X.append(point.getDim(0))
    #             Y.append(point.getDim(1))
    #
    #     if self.label == 1:
    #         return [1, 0, 0]
    #     elif self.label == 2:
    #         return [0, 1, 0]
    #     else:
    #         return [0, 0, 1]
    #             C.append(point.getColor())
    #
    #     return [X, Y, pointSize, C]