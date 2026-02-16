# 4. Use relational operators to check if a gene length is valid
#
# Expected Output:
# Invalid gene sequence

gene = "ATGCGTAC"
length = len(gene)
if length >= 3 and length % 3 == 0:
    print("Valid gene sequence")
else:
    print("Invalid gene sequence")
