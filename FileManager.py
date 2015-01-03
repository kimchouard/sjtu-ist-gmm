#import user class
from Set import SetClass
import csv

def importSet(path, dimension):
    s = SetClass()

    with open(path, "r") as f:
        data = csv.reader(f, delimiter=' ', skipinitialspace=True)

        for line in data:
            if (len(line) > 2):
                dataLabel = int(line[2])
            else:
                dataLabel = 0

            dims = [float(i) for i in line[:dimension]]
            s.add(dims, dataLabel)

    s.format()
    return s