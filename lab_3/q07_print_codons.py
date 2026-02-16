# Q7. Print codons (3 bases at a time).
#
# Expected Output:
# ATG
# CGA
# TAG
# CTA

dna = "ATGCGATAGCTA"
for i in range(0, len(dna), 3):
    print(dna[i:i + 3])
