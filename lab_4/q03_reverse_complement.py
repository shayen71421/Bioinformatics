# 3) Reverse complement of DNA
#
# Expected Output:
# Reverse complement: GTACGCAT

seq = "ATGCGTAC"
comp = {"A": "T", "T": "A", "G": "C", "C": "G"}
rev_comp = "".join(comp[b] for b in reversed(seq))
print("Reverse complement:", rev_comp)
