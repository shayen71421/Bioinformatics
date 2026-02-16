# 8. Calculate molecular weight of a peptide using operators
# (Simplified model: assume average amino-acid weight = 110 Da)
#
# Expected Output:
# Approx. Molecular Weight: 550 Da

peptide = "MKLTA"
aa_weight = 110
mw = len(peptide) * aa_weight
print("Approx. Molecular Weight:", mw, "Da")
