#import user class
from Point import PointClass
from Set import SetClass


def importSet(path):
    s = SetClass()

    with open(path, "r") as f:
        data = f.readlines()

        for line in data:
            words = line.split()
            if (len(words) > 2):
                label = int(words[2])
            else:
                label = 0
            s.add(PointClass([float(words[0]), float(words[1])], label))
    return s
