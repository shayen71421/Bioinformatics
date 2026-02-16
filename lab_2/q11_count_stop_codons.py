# 11) Count the stop codons in a sequence
#
# Expected Output:
# Number of stop codons: 2

dna = "ATGTAACTGTAGGGTGA"
stop_codons = {"TAA", "TAG", "TGA"}
count = 0

for i in range(0, len(dna), 3):
    codon = dna[i:i + 3]
    if codon in stop_codons:
        count += 1

print("Number of stop codons:", count)
