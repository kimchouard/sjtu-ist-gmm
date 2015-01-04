import numpy as np


def logN(X, MEAN, COV):
    """
    Evaluates natural log of the PDF for the multivariate Guassian distribution.
    """

    mean = MEAN
    x = X.T
    cov2d = np.atleast_2d(COV)  # So we also can use it for 1-d distributions

    N = len(MEAN)
    ex1 = np.dot(np.linalg.inv(cov2d), (x.T-mean).T)
    ex = -0.5 * (x.T-mean).T * ex1
    if ex.ndim == 2:
        ex = np.sum(ex, axis=0)
    K = -(N/2)*np.log(2*np.pi) - 0.5*np.log(np.linalg.det(COV))
    return ex + K

def gaussianPdf(X, MEAN, COV):
    """
    Evaluate the pdf of data to belong for the ith component of the mixture
    :param X:
    :param MEAN:
    :param COV:
    :return: (npArray) Proba for each data
    """
    d = len(MEAN)
    mean = MEAN
    x = np.array(X).T
    cov = np.atleast_2d(COV)

    ex1 = np.dot(np.linalg.inv(cov), (x.T-mean).T)
    ex = -0.5 * (x.T-mean).T * ex1
    ex = np.sum(ex, axis=0)
    K = 1 / np.sqrt(np.power(2*np.pi, d) * np.linalg.det(cov))
    return K*np.exp(ex)
