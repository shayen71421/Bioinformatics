# 5. Logical operators to check if a DNA sequence starts with ATG and ends with a stop codon
#
# Expected Output:
# It is a possible coding sequence

dna = "ATGACCTTATAG"
start = dna.startswith("ATG")
stop = dna.endswith(("TAA", "TAG", "TGA"))
if start and stop:
    print("It is a possible coding sequence")
else:
    print("Not a coding region")
