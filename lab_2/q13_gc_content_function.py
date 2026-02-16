# 13) Write a function to calculate GC content of a DNA sequence
#
# Expected Output:
# GC content (%): 55.00000000000001


def gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    return (g + c) / len(seq) * 100


dna = "ATGCGCGATCGATCGAATCG"
result = gc_content(dna)
print("GC content (%):", result)
