# Q9. Find the first stop codon.
#
# Expected Output:
# Stop codon at position: 9

dna = "ATGGCCGCTTAGGAT"
stop_codons = ["TAG", "TGA", "TAA"]

i = 0
while i < len(dna):
    codon = dna[i:i + 3]
    if codon in stop_codons:
        print("Stop codon at position:", i)
        break
    i += 3
