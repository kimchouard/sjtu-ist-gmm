import numpy as np
# import math
import FileManager
import GMMToolbox as GMM
from Set import SetClass


class EMalgo:
    def __init__(self, source, k, label=0):
        """
        Initialize with values set and # of comp. to search for, and init Teta.
        Params:
            s: SetClass containing the xn values OR string to the data file
            k: number of components to search for
            label: narrow to a specific label in the set if needed
        """

        # Initiate the s data Set, either from file or direct parameter
        if type(source) is str:
            self.s = FileManager.importSet(source, label)
        elif type(source) is SetClass:
            self.s = source
        else:
            errorMsg = "The 1st param should be either a str or a SetClass"
            raise TypeError(errorMsg)

        self.k = k

        #Deduce the dimension from the input
        self.d = self.s.getPoint(0).getDimNum()

    # Run the EM algorithm for the value sets, with k components
    def run(self):
        # Initialize Teta values
        self.initRun()
        self.describe()
        self.iterate()
        self.describe()

    def iterate(self):
        # Create new params
        # postProb = []
        postProbSum = 0
        postProbSums = []
        newMean = []
        newCov = []
        newWs = []

        for m in range(0, self.k):
            # Calculate each postProb along with its sum
            postProbM = []
            postProbSumM = 0
            for n in range(0, self.s.getLength()):
                xn = self.getXn(n)
                w = self.ws[self.it]
                mean = self.means[self.it]
                cov = self.covs[self.it]
                postProbMN = GMM.postProb(m, w, xn, mean, cov)
                postProbM.append(postProbMN)
                postProbSumM += postProbMN
            # postProb.append(postProbM)
            postProbSum += postProbSumM
            postProbSums.append(postProbSumM)

            # Calculate new mean
            newMeanM = 0
            n = 0
            for n in range(0, self.s.getLength()):
                newMeanM += np.dot(postProbM[n], self.getXn(n))
                n = n + 1
            newMeanM = newMeanM / postProbSumM
            newMean.append(newMeanM)

            # Calculate new cov
            newCovM = 0
            n = 0
            for n in range(0, self.s.getLength()):
                diff = np.subtract(self.getXn(n), newMeanM)
                rightDot = np.dot(diff, np.transpose(diff))
                newCovM += np.dot(postProbM[n], rightDot)
            newCov.append(newCovM)
            n = n + 1

        #Update weights
        for m in range(0, self.k):
            newWs.append(postProbSums[m]/postProbSum)

        # Add new params to history lists
        self.postProbs.append(postProbSums)
        self.means.append(newMean)
        self.covs.append(newCov)
        self.ws.append(newWs)

        # Increment the iteration count
        self.it += 1

    # Get the dim of a point at n
    def getXn(self, n):
        return self.s.getPoint(n).getDims()

    def initRun(self):
        """
        Initialize Tetas history and iteration counters for the EM alg
        Where: ws = [w1,...], means = [mean1,...], covs = [cov1,...]
        Comming from EM iterations
        """
        # Initialize iterations
        self.it = 0
        self.postProbs = []

        # Init weights
        w = np.ones(self.k) / self.k
        self.ws = [w]

        # Init mean (Harcoded for now)
        # TODO: found those automatically -> k-means
        mean = [[[-0.504032], [-0.0625]],
                [[0.780242], [1.46875]],
                [[1.5], [-0.015625]],
                [[2.54435], [0.9375]]]
        self.means = [mean]

        # Init covariance matrix with Identities
        cov = []
        for i in range(0, self.k):
            cov.append(np.identity(self.d))
        self.covs = [cov]

    def describe(self):
        print "On iteration ", self.it
        print "Data set: ", self.s.describe(False)
        print "K and D:", self.k, ",", self.d
        print "Post prob. matrix: ", self.postProbs
        print "Teta(w, mean, cov): "
        print self.ws[self.it]
        print self.means[self.it]
        print self.covs[self.it]
