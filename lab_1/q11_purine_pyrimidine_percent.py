# 11. Find the percentage of purines vs pyrimidines
# Purines = A + G
# Pyrimidines = C + T
#
# Expected Output:
# Purine %: 55.55555555555556
# Pyrimidine %: 44.44444444444444

dna = "AAGCTCGAT"
purines = dna.count("A") + dna.count("G")
pyrimidines = dna.count("C") + dna.count("T")
total = len(dna)
print("Purine %:", (purines / total) * 100)
print("Pyrimidine %:", (pyrimidines / total) * 100)
