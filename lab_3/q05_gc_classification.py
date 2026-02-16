# Q5. Classify GC content as High, Medium, or Low.
#
# Expected Output:
# Medium GC

dna = "ATGCGCGGTA"
gc = (dna.count("G") + dna.count("C")) / len(dna) * 100

if gc > 60:
    print("High GC")
elif gc > 40:
    print("Medium GC")
else:
    print("Low GC")
