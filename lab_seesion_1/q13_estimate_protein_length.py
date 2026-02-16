# 13. Write a Python program to estimate the protein length from an RNA sequence by
# translating codons into amino acids, where protein length = total number of codons - number of stop codons.
#
# Expected Output:
# Protein Length: 3

rna = "AUGGCCUAAUGG"
codons = len(rna) // 3
stop_codons = rna.count("UAA") + rna.count("UAG") + rna.count("UGA")
protein_len = codons - stop_codons
print("Protein Length:", protein_len)
