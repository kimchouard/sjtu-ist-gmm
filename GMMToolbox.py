import numpy as np
import math


# Exponential approach to calculate N
def N(xn, mean, cov):
    d = len(xn)
    if d == len(mean) and (d, d) == cov.shape:
        det = np.linalg.det(cov)
        if det == 0:
            raise NameError("The covariance matrix can't be singular")

        power = math.pow(det, 1.0/2)
        norm_const = 1.0/(math.pow((2*math.pi), float(d)/2) * power)
        xnMean = np.matrix(xn - mean)
        inv = cov.I
        expIn = -0.5 * (np.transpose(xnMean) * inv * xnMean)
        result = math.pow(math.e, expIn)
        return norm_const * result
    else:
        raise NameError("The dimensions of the input don't match")


# Log approach to calculate N
def logN(xn, mean, cov):
    # First deduce the dimension from the length of u (mean)
    d = len(mean)

    if (d, d) == cov.shape:
        det = np.linalg.det(cov)
        # Calc of the det
        det = np.linalg.det(cov)
        # Check covariance matrix
        if det == 0:
            raise NameError("The covariance matrix can't be singular")
        # Pre-calc of x - mean
        diff = xn - mean
        # Prec-cal of the first part of the sum
        part1 = d*np.log(2*math.pi)
        # Pre-calc of last part of the sum
        part3 = np.dot(np.transpose(diff), np.dot(np.linalg.inv(cov), diff))

        main = part1+np.log(det)+part3

        return -main/2
    else:
        raise NameError("The dimensions of the input don't match")


# DEBUG
# xn = np.matrix('0.6; 1.5')
# mean = np.matrix('0; 0')
# cov = np.matrix('1 0; 0 1')
# print math.exp(logN(xn, mean, cov))
# print N(xn, mean, cov)
