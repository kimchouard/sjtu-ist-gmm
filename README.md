# Expectation Maximisation with Gaussian Mixture Model

Project made by Kim Chouard in the context of Intelligent Speech processing class of Shanghai Jiao Tong University.

## Getting Started

Create a local environment:

```bash
virtualenv env
source env
source env/bin/activate
```

Then install the dependencies:
```bash
pip install -r requirements.txt
easy_install argparse
```

You can now run the script:
```bash
python main.py <training input file> <unlabeled input file> <labeled output file>
```