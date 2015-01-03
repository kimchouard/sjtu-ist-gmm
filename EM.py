import numpy as np
import random
import math
import GMMToolbox as GMM
from Set import SetClass


class EMmanager:
    """ A set of function to apply a Expectation Maximization algo,
    based on the Gaussian Mixture Models algorithm.

    Attrs:
    => for __init__
    - source:
    (SetClass) SetClass containing the xn values
    - K:
    (int) number of components to search for
    - d:
    (int) number of dimensions of the input

    => misc
    - it
    (int) the number of iterations done
    - w
    (npArray K) containing the weights.
    - mean
    (npArray K*d) containing the means.
    - cov
    (npArray K*d*d) containing the covs.
    - label:
    (str) label of the model, to narrow to a specific label in the set if needed
    """

    def __init__(self, source, k, label, eps=1e-8, maxIt=20):
        """
        Initialize with values set and # of comp. to search for, and init Teta.
        """

        # Store misc var in self
        self.K = k
        self.label = label
        self.d = source.getFeatures(label).shape[1]
        self.eps = eps
        self.maxIt = maxIt
        self.s = source

    def describe(self):
        print "On iteration ", self.it
        print "Data set: ", self.s.describe(False)
        print "K and D:", self.K, ",", self.d
        print "Teta(w, mean, cov): "
        print self.w
        print self.mean
        print self.cov

    def initRun(self):
        """
        Initialize Tetas history and iteration counters for the EM alg
        Where: ws = [w1,...], means = [mean1,...], covs = [cov1,...]
        Coming from EM iterations
        """
        # Initialize iterations
        self.it = 0

        # Init weights
        self.w = np.ones(self.K) / self.K

        # Init mean
        self.mean = self.initMean("hardcoded")


        # Init covariance matrix with Identities
        self.cov = []
        for i in range(0, self.K):
            self.cov.append(np.diag(np.ones(self.d)))

    def initMean(self, method):
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

    def train(self):
        """ Run the EM algorithm for the value sets, with k components """
        # Initialize Teta values
        self.initRun()

        # Init eps calculation
        logL = 0

        self.describe()
        # TODO do the iteration (for loop) on multiples labels
        for i in range(self.maxIt):
            # TODO check dat
            newLogL = self.EMiterate()

            if np.abs(logL - newLogL) < self.eps:
                break
            else:
                logL = newLogL
                self.it += 1
        self.describe()

    def EMiterate(self):
        """
        Do one iteration
        :return: logL
        """
        # Get params for current iteration
        data = self.s.getFeatures(self.label) #TODO check the matrix aspect

        nbSamples, nbFeatures = data.shape
        log_pXn_mat = np.zeros((nbSamples, self.K))
        for i in range(self.K):
            tmp = GMM.logN(data, self.mean[i], self.cov[i])
            log_pXn_mat[:, i] = tmp + np.log(self.w[i])
        pMax = np.max(log_pXn_mat, axis=1)
        log_pXn = pMax + np.log(np.sum(np.exp(log_pXn_mat.T - pMax), axis=0).T)
        logL = np.sum(log_pXn)

        log_pNk = np.zeros((nbSamples, self.K))
        for i in range(self.K):
            log_pNk[:, i] = log_pXn_mat[:, i] - log_pXn

        pNk = np.e**log_pNk

        for i in range(self.K):
            self.mean[i] = np.sum(pNk[:, i] * data.T, axis=1) / np.sum(pNk[:, i])
            self.cov[i] = np.dot(pNk[:, i] * (data - self.mean[i]).T, data - self.mean[i]) / np.sum(pNk[:, i])
            self.w[i] = np.sum(pNk[:, i]) / nbSamples

        return logL

    def wN(w, xn, mean, cov):
        """ Ponder N with its weight for the GMM """
        return w*math.exp(GMM.logN(xn, mean, cov))