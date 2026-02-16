# 10. Count nucleotides using variables and operators
#
# Expected Output:
# A: 4 T: 3 G: 3 C: 3
# Total: 13

dna = "ATGCCGATTAACG"
A = dna.count("A")
T = dna.count("T")
G = dna.count("G")
C = dna.count("C")
print("A:", A, "T:", T, "G:", G, "C:", C)
print("Total:", A + T + G + C)
