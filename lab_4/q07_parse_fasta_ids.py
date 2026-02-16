# 7) Parse FASTA file and print IDs and lengths
#
# Expected Output (example):
# ID: seq1 Length: 55
# ID: seq2 Length: 55

from Bio import SeqIO

for record in SeqIO.parse("example.fasta", "fasta"):
    print("ID:", record.id, "Length:", len(record.seq))
