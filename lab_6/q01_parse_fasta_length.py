# 1) Parse a FASTA file and print each sequence ID and its length.
#
# Expected Output (example):
# seq1 55
# seq2 55

from Bio import SeqIO

for record in SeqIO.parse("sample.fasta", "fasta"):
    seq_id = record.id
    length = len(record.seq)
    print(seq_id, length)
