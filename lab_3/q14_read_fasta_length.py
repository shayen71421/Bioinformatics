# Q14. Read a FASTA file and print sequence length.
#
# Expected Output (example):
# 110

f = open("seq.fasta")
lines = f.readlines()
seq = "".join(line.strip() for line in lines if not line.startswith(">"))
print(len(seq))
