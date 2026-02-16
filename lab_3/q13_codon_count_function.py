# Q13. Count codons.
#
# Expected Output:
# {'ATG': 1, 'CGA': 1, 'TGA': 1, 'TG': 1}


def codon_count(seq):
    counts = {}
    for i in range(0, len(seq), 3):
        codon = seq[i:i + 3]
        counts[codon] = counts.get(codon, 0) + 1
    return counts

print(codon_count("ATGCGATGATG"))
