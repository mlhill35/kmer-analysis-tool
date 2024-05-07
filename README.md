# K-Mer Analysis Tools

## Overview
This repository contains a collection of Python scripts designed to analyze k-mers in genetic sequences. These tools allow users to extract k-mers from sequences, aggregate k-mers from multiple sequences in a file, and determine the smallest `k` value for which each k-mer in a sequence has a unique subsequent k-mer.

## Features
- **find_kmers**: Function to extract k-mers from a given DNA sequence.
- **find_kmers_in_file**: Function to process multiple sequences from a file, extracting and aggregating k-mers.
- **smallest_k_with_unique_next**: Function to determine the smallest `k` such that every k-mer in a sequence has a unique subsequent k-mer.

## Installation
Clone this repository to your local machine to start working with the scripts:
```bash
git clone https://github.com/mlhill35/kmer-analysis-tool.git
cd kmer-analysis-tool
```

## Python Installation
Ensure Python is installed on your system. These scripts were developed using Python 3.8. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage
To run these scripts, navigate to the directory containing the scripts and use the following commands:
```bash
python3 -c 'import sys; from kmer_functions import find_kmers; print(find_kmers("ATGTCTGTCTGAA", 2))' # extracts k-mers from a sequence
python3 -c 'import sys; from kmer_functions import find_kmers_in_file; print(find_kmers_in_file("seq_file", 2))' # extracts and aggregates k-mers from a sequence file
python3 -c 'import sys; from kmer_functions import smallest_k_with_unique_next; print(smallest_k_with_unique_next("seq_file"))' # finds the smallest k with unique next k-mers
```

## Testing
This project uses pytest for testing. To run the tests, ensure you have pytest installed first before running the test functions:
```bash
pip install pytest
pytest tests/test_kmer.py # verifies correctness of implementations
```

## License
This project is licensed under the MIT License.

