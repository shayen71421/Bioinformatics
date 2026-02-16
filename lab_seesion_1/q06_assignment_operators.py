# 6. Using assignment operators to compute AT-content progressively
#
# Expected Output:
# AT Count: 6

dna = "AATGCTTAC"
a = dna.count("A")
t = dna.count("T")
at = 0
at += a
at += t
print("AT Count:", at)
