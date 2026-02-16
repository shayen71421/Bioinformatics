# 9) Filter sequences based on length
#
# Expected Output:
# Analyzing: ATGCGT
# Analyzing: AATTGGCC

seqs = ["ATG", "ATGCGT", "AATTGGCC"]
for s in seqs:
    if len(s) < 5:
        continue
    print("Analyzing:", s)
