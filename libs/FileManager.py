#import user class
from Set import SetClass
import csv

def importSet(path, dimension):
    s = SetClass()

    with open(path, "r") as f:
        data = csv.reader(f, delimiter=' ', skipinitialspace=True)

        for line in data:
            if (len(line) > 2):
                dataLabel = line[2]
            else:
                dataLabel = "-1"

            dims = [float(i) for i in line[:dimension]]
            s.add(dims, dataLabel)
    # Finalize the set with an array form
    s.format()
    return s

def exportSet(path, set):
    with open(path, 'w') as f:
        for label in set.getLabels():
            for i, sample in enumerate(set.getFeatures(label)):
                sample = ["{0:.6f}".format(j) for j in set.getFeatures(label)[i]]
                sample = " ".join(sample)
                f.write(sample + "  " + label + "\n")