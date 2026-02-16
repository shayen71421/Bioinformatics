# 6) Translate DNA to protein (Biopython)
#
# Expected Output:
# Protein sequence: MAIVMGR*KGAR*

from Bio.Seq import Seq

dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
protein = dna.translate()
print("Protein sequence:", protein)
