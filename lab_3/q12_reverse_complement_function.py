# Q12. Reverse complement function.
#
# Expected Output:
# ACGCAT


def rev_comp(seq):
    comp = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(comp[b] for b in seq)[::-1]

print(rev_comp("ATGCGT"))
