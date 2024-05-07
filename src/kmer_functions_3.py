import sys

def find_kmers(sequence, k):
    kmers = {}
    length = len(sequence)
    # iterates through the sequence to extract k-mers
    for i in range(length - k + 1):
        kmer = sequence[i:i+k]
        next_index = i + 1
        # checks if there is a subsequent k-mer to consider
        if next_index < length - k + 1:
            next_kmer = sequence[next_index:next_index+k]
            # adds the subsequent k-mer to the set associated with the k-mer key
            kmers.setdefault(kmer, set()).add(next_kmer)
        elif kmer not in kmers:
            # adds the last k-mer with an empty set if it has not been added yet
            kmers[kmer] = set()
    return kmers

# example usage via console or command line:
# result = find_kmers('ATGTCTGTCTGAA', 2)
# print(result)

def find_kmers_in_file(filename, k):
    all_kmers = {}
    # opens the file for reading
    with open(filename, 'r') as file:
        # reads each line in the file
        for line in file:
            line = line.strip()
            # checks that the line is not empty
            if line:
                kmers = find_kmers(line, k)
                # aggregates k-mers and their subsequent k-mers from the file
                for kmer, next_kmers in kmers.items():
                    if kmer in all_kmers:
                        all_kmers[kmer].update(next_kmers)
                    else:
                        all_kmers[kmer] = next_kmers.copy()
    return all_kmers

# example usage via console or command line:
# result = find_kmers_in_file("seq_file", 2)
# print(result)

def smallest_k_with_unique_next(filename):
    with open(filename, 'r') as file:
        sequence = file.read().strip()
    max_k = len(sequence)
    # iterates through possible k values to find the smallest k with unique subsequent k-mers
    for k in range(1, max_k + 1):
        kmers = find_kmers_in_file(filename, k)
        # checks if all k-mers have exactly one unique subsequent k-mer
        if all(len(next_kmers) == 1 for next_kmers in kmers.values() if next_kmers):
            return k
    return None

# example usage via console or command line:
# result = smallest_k_with_unique_next("seq_file")
# print(result)

# EXAM QUESTION:
# result = smallest_k_with_unique_next("../../../shared/439539/reads.fa")
# print(result)  
# answer: 10
