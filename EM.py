import numpy as np
import random
import math
import FileManager
import GMMToolbox as GMM
from Set import SetClass


class EMalgo:
    """ A set of function to apply a Expectation Maximization algo,
    based on the Gaussian Mixture Models algorithm.

    Attrs:
    => for __init__
    - source:
    1. (str) string to the data file ---> then transformed into a SetClass
    2. (SetClass) SetClass containing the xn values
    - K:
    (int) number of components to search for
    - d:
    (int) number of dimensions of the input

    => misc
    - it
    (int) the number of iterations done
    - postProbs
    (list) containing all the posterior probability for each iteration.
    - ws
    (npArray K) containing the weights for each iteration.
    - means
    (npArray K*d) containing the mean for each iteration.
    - covs
    (npArray K*d*d) containing the covs for each iteration.
    - label:
    (str) label of the model, to narrow to a specific label in the set if needed
    """

    def __init__(self, source, k, dim, label):
        """
        Initialize with values set and # of comp. to search for, and init Teta.
        """

        # Store misc var in self
        self.K = k
        self.label = label
        self.d = dim

        # Initiate the s data Set, either from file or direct parameter
        if type(source) is str:
            self.s = FileManager.importSet(source, self.d)
        elif type(source) is SetClass:
            self.s = source
        else:
            errorMsg = "The 1st param should be either a str or a SetClass"
            raise TypeError(errorMsg)

    def describe(self):
        print "On iteration ", self.it
        print "Data set: ", self.s.describe(False)
        print "K and D:", self.K, ",", self.d
        print "Teta(w, mean, cov): "
        print self.ws[self.it]
        print self.means[self.it]
        print self.covs[self.it]

    def initRun(self):
        """
        Initialize Tetas history and iteration counters for the EM alg
        Where: ws = [w1,...], means = [mean1,...], covs = [cov1,...]
        Coming from EM iterations
        """
        # Initialize iterations
        self.it = 0

        # Init weights
        w = np.ones(self.K) / self.K
        self.ws = [np.array(w)]

        # Init mean
        self.means = [self.initMeans("hardcoded")]


        # Init covariance matrix with Identities
        cov = []
        for i in range(0, self.K):
            cov.append(np.diag(np.ones(self.d)))
        self.covs = [np.array(cov)]

    def initMeans(self, method):
        """
        Init the first means, following different methods.

        :param method:
        Define the method to use. Either:
        - hardcoded,
        - random (todo),
        - kmeans.
        :return: array with first mean
        """
        if method == "hardcoded":
            mean = np.matrix([[-0.504032, -0.0625],
                              [0.780242, 1.46875],
                              [1.5, -0.015625],
                              [2.54435, 0.9375]])
        elif method == "random":
            # TODO: test random
            mean = random.sample(self.s.getFeatures, self.K)
        elif method == "kmeans":
            # TODO: found those automatically -> k-means
            raise Exception("Method not implemented")

        # DEBUG
        # print "DEBUG"
        # print mean
        # meanA = [[[-0.504032], [-0.0625]],
        #         [[0.780242], [1.46875]],
        #         [[1.5], [-0.015625]],
        #         [[2.54435], [0.9375]]]
        # print meanA

        return np.array(mean)

    def getXn(self, n):
        """
        Get the dim of a point at n
        :param n:
        :return:
        """
        return self.s.getPoint(n).getDims()

    def run(self, eps=1e-8, maxIt=1):
        """ Run the EM algorithm for the value sets, with k components """
        # Initialize Teta values
        self.initRun()
        self.describe()
        # TODO do the iteration (for loop)
        for i in range(maxIt):
            # TODO check dat
            self.EMiterate()
            self.describe()

            # TODO break when diff under eps
            # Increment the iteration count
            self.it += 1

    def EMiterate(self):
        # Get params for current iteration
        data = self.s.getFeatures(self.label) #TODO check the matrix aspect
        w = self.ws[self.it]
        mean = self.means[self.it]
        cov = self.covs[self.it]

        nbSamples, nbFeatures = data.shape
        log_pXn_mat = np.zeros((nbSamples, self.K))
        for i in range(self.K):
            tmp = GMM.logN(data, mean[i], cov[i])
            log_pXn_mat[:, i] = tmp + np.log(w[i])
        pMax = np.max(log_pXn_mat, axis=1)
        log_pXn = pMax + np.log(np.sum(np.exp(log_pXn_mat.T - pMax), axis=0).T)
        logL = np.sum(log_pXn)

        log_pNk = np.zeros((nbSamples, self.K))
        for i in range(self.K):
            log_pNk[:, i] = log_pXn_mat[:, i] - log_pXn

        pNk = np.e**log_pNk

        # Create new params
        newMean = np.zeros(4)
        newCov = np.zeros(4)
        newWs = np.zeros(4)

        for i in range(self.K):
            newMean[i] = np.sum(pNk[:, i] * data.T, axis=1) / np.sum(pNk[:, i])
            newCov[i] = np.dot(pNk[:, i] * (data - mean[i]).T, data - mean[i]) / np.sum(pNk[:, i])
            newWs[i] = np.sum(pNk[:, i]) / nbSamples

        # Add new params to history lists
        self.means.append(newMean)
        self.covs.append(newCov)
        self.ws.append(newWs)
        # return (means, cov, weights, logL)

    def wN(w, xn, mean, cov):
        """ Ponder N with its weight for the GMM """
        return w*math.exp(GMM.logN(xn, mean, cov))