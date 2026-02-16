# 3. Use arithmetic operators to calculate GC content
#
# Expected Output:
# GC Content: 58.333333333333336 %

dna = "ATGCGCGGCTTA"
g = dna.count("G")
c = dna.count("C")
gc_content = ((g + c) / len(dna)) * 100
print("GC Content:", gc_content, "%")
