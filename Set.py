import numpy as np
import matplotlib.pyplot as plt

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
            print "Containing %d points on label %s." % (len(self.dataDic[label]), label)
            if full:
                for point in self.dataDic[label]:
                    print "1,"+str(point)

    def getPlotData(self):
        """
        Get plot data for matplotlib
        (only support 2 dims for now)
        :return: [X, Y, pointSize, Colors]
        """
        X = []
        Y = []
        pointSize = 5
        C = []

        for label in self.dataDic:
            for point in self.dataDic[label]:
                X.append(point[0])
                Y.append(point[1])

            if label == 1:
                C.append([1, 0, 0])
            elif label == 2:
                C.append([0, 1, 0])
            else:
                C.append([0, 0, 1])

        return [X, Y, pointSize, C]

    def plot(self):
        data = self.getPlotData()
        plt.scatter(data[0], data[1], data[2], data[3])
        plt.show()