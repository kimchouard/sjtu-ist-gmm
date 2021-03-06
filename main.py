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
        help='Means selection method: `random` `kmeans` (not yet implemented).',
        required=False,
        default="random"
    )
    command.add_argument(
        '-v',
        '--verbose',
        help='Get it more talkative :)',
        action='store_true'
    )
    command.add_argument(
        '-t',
        '--tests',
        help='Used to test the algorithm. Don\'t import the labels from the unlabeled'
             ' input file, even if labeled.',
        action='store_true'
    )

    args = command.parse_args()

    if args.verbose:
        print '====== Start reading training file ========='

    if not path.isfile(args.training) or not path.isfile(args.file):
        command.error('Invalid file path')

    # Create the Set from the training inputFile
    sTrain = FM.importSet(args.training, args.dimension)

    if args.verbose:
        print '======= Reading training file done ========='
        print '============= Start training ==============='

    # Init the model array
    models = []

    for label in sTrain.getLabels():
        model = EMmanager(sTrain, 4, label, args.verbose)
        model.train(args.initMethod)
        models.append(model)

    if args.verbose:
        print '============= Training done ================'
        print '========= Start label affectation =========='

    s2label = FM.importSet(args.file, args.dimension, args.tests)
    s2label.affectLabel(models)

    if args.verbose:
        print '========= Label affectation done ==========='
        print '========== Start writing output ============'

    FM.exportSet(args.output, s2label)

    if args.verbose:
        print '========== Writing output done ============='

if __name__ == '__main__':
    main()
