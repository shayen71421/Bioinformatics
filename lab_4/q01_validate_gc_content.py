# 1) Validate DNA and compute GC content
#
# Expected Output (sample input ATGCGC):
# GC Content (%): 66.66666666666666

dna = input("Enter DNA sequence: ").upper()
valid_bases = {"A", "T", "G", "C"}

if all(base in valid_bases for base in dna):
    gc_count = dna.count("G") + dna.count("C")
    print("GC Content (%):", (gc_count / len(dna)) * 100)
else:
    print("Invalid DNA sequence!")
