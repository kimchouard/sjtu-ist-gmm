#! /usr/bin/env python

from EM import EMmanager
import FileManager


def main():
    s = FileManager.importSet("data/train.txt", 2)
    s.plot()

    model = EMmanager(s, 4, 2)
    model.train()

if __name__ == '__main__':
    main()
