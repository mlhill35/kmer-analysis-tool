import os
import tempfile
import pytest
from kmer_functions_3 import find_kmers, find_kmers_in_file, smallest_k_with_unique_next

def test_find_kmers():
    """
    Tests the find_kmers function to ensure it correctly identifies k-mers and their subsequent k-mers in a given sequence.
    """
    sequence = "ATGTCTGTCTGAA"
    k = 2
    expected = {'AT': {'TG'}, 'TG': {'GT', 'GA'}, 'GT': {'TC'}, 'TC': {'CT'}, 'CT': {'TG'}, 'GA': {'AA'}, 'AA': set()}
    result = find_kmers(sequence, k)
    assert result == expected

def test_find_kmers_large():
    """
    Tests the find_kmers function with a k value larger than the sequence length to ensure it returns an empty dictionary.
    """
    sequence = "ATGT"
    k = 5
    expected = {}  # Expect an empty dictionary because k is larger than the sequence length
    result = find_kmers(sequence, k)
    assert result == expected

def test_find_kmers_in_file():
    """
    Tests the find_kmers_in_file function by writing a test sequence to a temporary file, then checks if k-mers are correctly identified.
    """
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as tmp:
        tmp.write("ATGTCTGTCTGAA")
        tmp_name = tmp.name

    result = find_kmers_in_file(tmp_name, 2)
    expected = {'AT': {'TG'}, 'TG': {'GT', 'GA'}, 'GT': {'TC'}, 'TC': {'CT'}, 'CT': {'TG'}, 'GA': {'AA'}, 'AA': set()}
    assert result == expected
    os.remove(tmp_name)  # Clean up: remove the temporary file after the test

def test_smallest_k_with_unique_next():
    """
    Tests the smallest_k_with_unique_next function by writing a test sequence to a temporary file, 
    then checking if the function correctly determines the smallest k for which all k-mers are followed by a unique subsequent k-mer.
    """
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as tmp:
        tmp.write("ATGTCTGTCTGAA")
        tmp_name = tmp.name

    result = smallest_k_with_unique_next(tmp_name)
    assert result == 7  # Expected to find that k=7 produces unique subsequent k-mers
    os.remove(tmp_name)  # Clean up: remove the temporary file after the test

if __name__ == "__main__":
    pytest.main()
