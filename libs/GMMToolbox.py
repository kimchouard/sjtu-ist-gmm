import numpy as np
import math


# Exponential approach to calculate N, gaussian dist. for xn
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


# Log approach to calculate N, gaussian dist. for xn
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
        diff = np.subtract(xn, mean)
        # Prec-cal of the first part of the sum
        part1 = d*np.log(2*math.pi)
        # Pre-calc of last part of the sum
        part3 = np.dot(np.transpose(diff), np.dot(np.linalg.inv(cov), diff))

        main = part1+np.log(det)+part3

        return -main/2
    else:
        raise NameError("The dimensions of the input don't match")


# Ponder N with its weight for the GMM
def wN(w, xn, mean, cov):
    return w*math.exp(logN(xn, mean, cov))


# Calculate the posterior probability of xn for the comp. m
# *Glob var contains values for all components
def postProb(m, wGlob, xn, meanGlob, covGlob):
    # TODO: check all the Glob var has the same number of items
    # if (len(cGlob) == len(meanGlob)) and (covGlob.shape == len(cGlob)

    # Calc. the weighted N for the current component, top of the fraction
    curM = wN(wGlob[m], xn, meanGlob[m], covGlob[m])

    # Calc. the weighted N for all components, bottom of the fraction
    allM = 0
    j = 0
    for w in wGlob:
        allM += wN(w, xn, meanGlob[j], covGlob[j])
        j += 1

    return curM/allM

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