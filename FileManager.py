#import user class
from Point import PointClass
from Set import SetClass


def importSet(path, label=0):
    s = SetClass()

    with open(path, "r") as f:
        data = f.readlines()

        for line in data:
            words = line.split()
            if (len(words) > 2):
                dataLabel = int(words[2])
            else:
                dataLabel = 0

            # Narrow to a specific label, if needed
            if (label == 0) or (dataLabel == label):
                s.add(PointClass([float(words[0]), float(words[1])], dataLabel))
    return s
