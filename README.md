# chemreps
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation Status](https://readthedocs.org/projects/chemreps/badge/?version=latest)](https://chemreps.readthedocs.io/en/latest/?badge=latest)

chemreps is a Python package for the creation of molecular representations for the purpose of machine learning. The molecular representations included in this library are implemented/adapted from current literature. The aim of chemreps is to provide an easy to use library for making molecular representations that can be then used with machine learning packages such as Scikit-Learn and Tensorflow.

## Current Implementations
- Coulomb Matrix
- Bag of Bonds
- Bonds/Nonbonding, Angles, Torsions
- Just Bonds

The citations for the literature from which the representations are implemented/adapted from can be found in the source code for each representation.

## Representation requests
Requests for new representations to be added can be made by raising an issue and labeling it as a feature request. Before requesting a new representation, please check under the Representation project in the Projects tab to see if that representation is included in the current work or progress.

## Install
The latest release version can be installed with:
```
pip install chemreps
```

The latest development version can be installed by:
```
git clone https://github.com/dlf57/chemreps
cd chemreps
pip install -e .
```

#### Dependencies
chemreps requires:
- Python
- NumPy (>=1.12)
- cclib (>=1.5)

## Contributing
If you are interested in helping develop for this project, please check out [Contributing to chemreps](https://github.com/dlf57/chemreps/wiki/Contributing-to-chemreps) in the wiki for a guide on how how to get started.

## Disclaimers:
- These are attempts at the recreation of molecular representations from literature and may not be implemented properly.
    - If we do not implement something properly, feel free to make an issue.
- This is solely a representation library and will not perform machine learning.
