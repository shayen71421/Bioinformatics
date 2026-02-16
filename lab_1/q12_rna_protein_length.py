# 12. Convert RNA to protein length estimation
# (Codon -> amino acid; length = total codons - stop codons)
#
# Expected Output:
# Protein Length (approx): 3

rna = "AUGGCCUAAUGG"
codons = len(rna) // 3
stop_codons = rna.count("UAA") + rna.count("UAG") + rna.count("UGA")
protein_len = codons - stop_codons
print("Protein Length (approx):", protein_len)
