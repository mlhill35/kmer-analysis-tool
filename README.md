# K-Mer Analysis Tools

## Overview
# This repository contains a collection of Python scripts designed to analyze k-mers in genetic sequences. These tools allow users to extract k-mers from sequences, aggregate k-mers from multiple sequences in a file, and determine the smallest `k` value for which each k-mer in a sequence has exactly one unique subsequent k-mer.

## Features
- **find_kmers**: Function to extract k-mers from a given DNA sequence.
- **find_kmers_in_file**: Function to process multiple sequences from a file, extracting and aggregating k-mers.
- **smallest_k_with_unique_next**: Function to determine the smallest `k` such that every k-mer in a sequence has a unique subsequent k-mer.

## Installation
# Clone this repository to your local machine to start working with the scripts:
```bash
git clone https://github.com/mlhill35/kmer-analysis-tool.git
cd kmer-analysis-tool

# Ensure Python is installed on your system. These scripts were developed using Python 3.8
```bash
pip install -r requirements.txt

## Usage
# To run these scripts, navigate to the directory containing the scripts and use the following commands:

# To extract k-mers from a sequence:
```bash
python3 -c 'import sys; from kmer_functions import find_kmers; print(find_kmers("ATGTCTGTCTGAA", 2))'

# To extract and aggregate k-mers from a file:
```bash
python3 -c 'import sys; from kmer_functions import find_kmers_in_file; print(find_kmers_in_file("seq_file", 2))'

# To find the smallest k with unique next k-mers:
```bash
python3 -c 'import sys; from kmer_functions import smallest_k_with_unique_next; print(smallest_k_with_unique_next("seq_file"))'

## Testing
# This project uses pytest for testing. To run the tests, ensure you have pytest installed:
```bash
pip install pytest

# Then run tests with:
```bash
pytest tests/tes_kmer.py

# This will execute the tests defined in the test_kmer.py file, verifying the correctness of the implementations.

## License
# This project is licensed under the MIT License.
