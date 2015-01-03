#! /usr/bin/env python

from libs.EM import EMmanager
import libs.FileManager as FM


def main():
    s = FM.importSet("data/train.txt", 2)
    # s.plot()

    model = EMmanager(s, 4, 2)
    model.train()

if __name__ == '__main__':
    main()
