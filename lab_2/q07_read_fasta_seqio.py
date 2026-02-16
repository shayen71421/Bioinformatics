# 7) Read a FASTA file and print sequence ID and length (Biopython SeqIO)
#
# Expected Output (example):
# ID: seq1 Length: 100
# ID: seq2 Length: 95

from Bio import SeqIO

for record in SeqIO.parse("example.fasta", "fasta"):
    print("ID:", record.id, "Length:", len(record.seq))
