import numpy as np


def logN(X, MU, SIGMA):
    """
    Evaluates natural log of the PDF for the multivariate Guassian distribution.
    """

    mu = MU
    x = X.T
    sigma = np.atleast_2d(SIGMA)  # So we also can use it for 1-d distributions

    N = len(MU)
    ex1 = np.dot(np.linalg.inv(sigma), (x.T-mu).T)
    ex = -0.5 * (x.T-mu).T * ex1
    if ex.ndim == 2:
        ex = np.sum(ex, axis=0)
    K = -(N/2)*np.log(2*np.pi) - 0.5*np.log(np.linalg.det(SIGMA))
    return ex + K


# DEBUG
# m = 0
# w = [0.25, 0.25, 0.25, 0.25]
# xn = [[0.6], [1.5]]
# mean = [[[-0.504032], [-0.0625]],
#         [[0.780242], [1.46875]],
#         [[1.5], [-0.015625]],
#         [[2.54435], [0.9375]]]
# cov = []
# for i in range(0, 4):
#     cov.append(np.identity(2))
# print m, w, xn, mean, cov
# print postProb(m, w, xn, mean, cov)
# mean = np.matrix('0; 0')
# cov = np.matrix('1 0; 0 1')
# print math.exp(logN(xn, mean, cov))
# print N(xn, mean, cov)
