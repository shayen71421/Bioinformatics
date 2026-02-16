# Q8. Translate codons into amino acids (simplified dictionary).
#
# Expected Output:
# M
# A
# Stop

codon_table = {
    "ATG": "M", "GCT": "A", "TGA": "Stop"
}

dna = "ATGGCTTGA"
for i in range(0, len(dna), 3):
    codon = dna[i:i + 3]
    print(codon_table.get(codon, "?"))
