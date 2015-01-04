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

### Test script

To run a batch of test, on the dev.txt for examples:

```bash
python scripts/tests.py <training input file> <testing input file> <result output file> <number of iterations>
```