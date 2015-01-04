#! /usr/bin/env python

import sys
import subprocess
import re
import time
import csv

outputFile = 'data/tempOutput.txt'

def executeCmd(trainingData, testData, verbose=False, method=None):
    cmd = ['python', 'main.py', trainingData, testData, outputFile, '-t']
    if verbose:
        cmd.append('-v')
    if method is not None:
        cmd.append('-m')
        cmd.append(method)
    begin = time.time()
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, err = p.communicate()
    end = time.time()
    return end - begin, out, err


def diffFile(f1, f2):
    diffCmd = ['diff', '-y', '--suppress-common-lines', f1, f2]
    diff = subprocess.Popen(diffCmd, stdout=subprocess.PIPE)
    countLine = subprocess.Popen(['wc', '-lc'],
                                 stdin=diff.stdout, stdout=subprocess.PIPE)
    output = countLine.communicate()[0]
    count = re.search(r'[0-9]+', output)
    return int(count.group(0))


def getFileLength(f):
    cat = subprocess.Popen(['cat', f], stdout=subprocess.PIPE)
    countLine = subprocess.Popen(['wc', '-lc'],
                                 stdin=cat.stdout, stdout=subprocess.PIPE)
    output = countLine.communicate()[0]
    count = re.search(r'[0-9]+', output)
    return int(count.group(0))


def main(trainingData, testData, runs, csv):
    # Write csv header
    csv.writerow(["method", "errorRate", "time"])
    nbSamples = getFileLength(testData)
    methods = ["random"]
    for m in methods:
        print "\n#", m
        for i in range(runs):
            print".",
            res = executeCmd(trainingData, testData, method=m)
            if res[2] is not None:
                print res[2]
            nbDiff = diffFile(testData, outputFile)
            errorRate = (float(nbDiff) / nbSamples)*100
            row = [m, errorRate, res[0]]
            csv.writerow(row)


if __name__ == '__main__':
    if len(sys.argv) != 5:
        raise Exception("Specify training, test and result file and the number of runs")

    trainingData = sys.argv[1]
    testData = sys.argv[2]
    resultData = sys.argv[3]
    runs = int(sys.argv[4])
    with open(resultData, 'wb') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')
        main(trainingData, testData, runs, csvWriter)
