# 10) Search for a given motif in a DNA sequence and report positions
#
# Expected Output:
# Motif found at positions: [4, 10]

dna = "AAATGCGTATGCGTAC"
motif = "GCG"
positions = []

for i in range(len(dna) - len(motif) + 1):
    if dna[i:i + len(motif)] == motif:
        positions.append(i)

print("Motif found at positions:", positions)
