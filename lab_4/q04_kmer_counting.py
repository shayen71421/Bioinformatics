# 4) k-mer counting (subsequences of length k)
#
# Expected Output:
# k-mer counts: {'ATG': 2, 'TGC': 2, 'GCG': 2, 'CGT': 2, 'GTA': 1, 'TAT': 1}

dna = "ATGCGTATGCGT"
k = 3
kmer_counts = {}

for i in range(len(dna) - k + 1):
    kmer = dna[i:i + k]
    kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1

print("k-mer counts:", kmer_counts)
