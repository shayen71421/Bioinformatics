# Q10. Count GC until GC count reaches 5.
#
# Expected Output:
# First 5 GC positions scanned: 7

dna = "ATGCGCGCGTAG"
count = 0
i = 0

while i < len(dna) and count < 5:
    if dna[i] in ["G", "C"]:
        count += 1
    i += 1

print("First 5 GC positions scanned:", i)
