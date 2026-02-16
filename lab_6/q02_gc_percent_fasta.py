# 2) Compute GC% of each sequence in a FASTA file.
#
# Expected Output (example):
# seq1 GC% = 49.09
# seq2 GC% = 32.73

from Bio import SeqIO

for record in SeqIO.parse("sample.fasta", "fasta"):
    seq = record.seq.upper()
    gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    print(record.id, f"GC% = {gc:.2f}")
