#! /usr/bin/env python

#import user class
# from Point import PointClass
# from Set import SetClass
# import Plot
from EM import EMalgo


def main():
    # s.describe(False)
    # Plot.plotSet(s)
    em = EMalgo("data/train.txt", 4, 2)
    em.run()

if __name__ == '__main__':
    main()
