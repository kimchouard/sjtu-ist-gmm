# Expectation Maximisation with Gaussian Mixture Model

Project made by Kim Chouard in the context of Intelligent Speech processing class of Shanghai Jiao Tong University.

## Getting Started

Create a local environment:

```bash
virtualenv env
source env/bin/activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
easy_install argparse
```

## Usage

### Main script

To run the main script:

```bash
python main.py <training input file> <unlabeled input file> <labeled output file>
```

Optional arguments:

```
-h, --help            show a help message and exit
-d DIMENSION, --dimension DIMENSION
                      Number of dimensions for features
-m INITMETHOD, --initMethod INITMETHOD
                      Means selection method: `random` `kmeans` (not yet implemented).
-v, --verbose         Get it more talkative :)
-t, --tests           Used to test the algorithm. Don't import the labels from the unlabeled input file, even if labeled.
```

### Test script

To run a batch of test, on the dev.txt for examples:

```bash
python scripts/tests.py <training input file> <testing input file> <result output file> <number of iterations>
```