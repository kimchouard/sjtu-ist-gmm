import numpy as np
# import math


class EMalgo:
    # Initialize with values set and # of comp. to search for, and init Teta
    def __init__(self, s, k):
        self.s = s
        self.k = k
        print self.s.getPoint(0)
        #Deduce the dimension from the input
        self.d = self.s.getPoint(0).getDimNum()

    # Run the EM algorithm for the value sets, with k components
    def run(self):
        # Initialize Teta values
        self.initTeta()

        self.describe()
        #TODO: rest of the algorithm

    # Initialize Teta = (w, mean, cov) for the EM alg
    def initTeta(self):
        # Init weights
        self.w = np.ones(4) / self.k

        # Init mean (Harcoded for now)
        # TODO: found those automatically -> k-means
        self.mean = [[[-0.504032], [-0.0625]],
                    [[0.780242], [1.46875]],
                    [[1.5], [-0.015625]],
                    [[2.54435], [0.9375]]]

        # Init covariance matrix with Identities
        self.cov = []
        for i in range(0, self.k):
            self.cov.append(np.identity(self.d))

    def describe(self):
        print "Data set: ", self.s.describe(False)
        print "K and D", self.k, "\n", self.d, "\n"
        print "Teta(w, mean, cov): "
        print self.w, "\n", self.mean, "\n", self.cov, "\n"
