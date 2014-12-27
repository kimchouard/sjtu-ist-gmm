"""
Simple demo of a scatter plot.
"""
# import numpy as np
import matplotlib.pyplot as plt


def plotSet(s):
    data = s.getPlotData()
    plt.scatter(data[0], data[1], data[2], data[3])
    plt.show()
