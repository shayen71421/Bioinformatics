# Q17. Reading FASTA using SeqIO.
#
# Expected Output (example):
# seq1 55
# seq2 55

from Bio import SeqIO

for record in SeqIO.parse("seq.fasta", "fasta"):
    print(record.id, len(record.seq))
