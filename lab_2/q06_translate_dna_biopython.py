# 6) Translate DNA to Protein (using Biopython)
#
# Expected Output:
# Protein sequence: MAIVMGR*KGAR*

from Bio.Seq import Seq

dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
protein = dna.translate()
print("Protein sequence:", protein)
