# Q4. Check if DNA has EcoRI site (GAATTC).
#
# Expected Output:
# EcoRI site present

dna = "ATGGAATTCTAGC"
if "GAATTC" in dna:
    print("EcoRI site present")
else:
    print("EcoRI site absent")
