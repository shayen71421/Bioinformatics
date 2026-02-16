# 3) Convert a DNA sequence to protein using Biopython.
#
# Expected Output:
# MAIVMGR*KGAR*

from Bio.Seq import Seq

dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
protein = dna.translate()
print(protein)
