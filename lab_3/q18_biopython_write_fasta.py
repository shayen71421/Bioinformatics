# Q18. Writing a FASTA file.
#
# Expected Output:
# Writes output.fasta

from Bio import SeqIO

record = next(SeqIO.parse("seq.fasta", "fasta"))
SeqIO.write(record, "output.fasta", "fasta")
