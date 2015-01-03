#! /usr/bin/env python

# import user class
# from Point import PointClass
# from Set import SetClass
# import Plot
from EM import EMmanager
import FileManager


def main():
    s = FileManager.importSet("data/train.txt", 2)

    model = EMmanager(s, 4, 2)
    model.train()

if __name__ == '__main__':
    main()
