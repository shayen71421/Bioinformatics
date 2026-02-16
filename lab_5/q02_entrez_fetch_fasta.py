# 2) Use Biopython Entrez to retrieve a nucleotide sequence by accession
# and display the FASTA sequence.
#
# Expected Output (example):
# >ACCESSION ...
# ATG...
#
# Note: Requires internet access and a valid email address.

from Bio import Entrez, SeqIO

Entrez.email = "shayen224809@sahrdaya.ac.in"
accession = "NM_000546"

handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
handle.close()

print(record.format("fasta"))
