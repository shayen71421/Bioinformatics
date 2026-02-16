# 2) Nucleotide frequency counter
#
# Expected Output:
# Nucleotide counts: {'A': 2, 'T': 2, 'G': 4, 'C': 2}

seq = "ATGCCGTAGG"
counts = {"A": 0, "T": 0, "G": 0, "C": 0}

for base in seq:
    counts[base] += 1

print("Nucleotide counts:", counts)
