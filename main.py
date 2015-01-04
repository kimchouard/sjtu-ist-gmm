#! /usr/bin/env python

import argparse
from os import path

from libs.EM import EMmanager
import libs.FileManager as FM


def main():
    command = argparse.ArgumentParser(
        description='Expectation algorithm for Gaussian Mixture model.'
    )
    command.add_argument(
        'training',
        help='Training input file'
    )
    command.add_argument(
        'file',
        help='Unlabeled input file'
    )
    command.add_argument(
        'output',
        help='Labeled output file'
    )
    command.add_argument(
        '-d',
        '--dimension',
        help='Number of dimensions for features',
        required=False,
        type=int,
        default=2
    )
    command.add_argument(
        '-m',
        '--initMethod',
        help='Means selection method: `random` `kmeans` or `hardcoded`.',
        required=False,
        default="hardcoded"
    )
    command.add_argument(
        '-v',
        '--verbose',
        help='Get it more talkative :)',
        action='store_true'
    )

    args = command.parse_args()

    if not path.isfile(args.training) or not path.isfile(args.file):
        command.error('Invalid file path')

    # Create the Set from the training inputFile
    sTrain = FM.importSet(args.training, args.dimension)

    # Init the model array
    models = []

    for label in sTrain.getDataDic():
        model = EMmanager(sTrain, 4, label)
        model.train(args.initMethod)
        models.append(model)

    if args.verbose:
        print '============= Training done ================'

if __name__ == '__main__':
    main()
