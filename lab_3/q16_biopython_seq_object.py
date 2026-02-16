# Q16. Basic Biopython sequence object.
#
# Expected Output:
# TACGCATG
# GTACGCAT

from Bio.Seq import Seq

dna = Seq("ATGCGTAC")
print(dna.complement())
print(dna.reverse_complement())
