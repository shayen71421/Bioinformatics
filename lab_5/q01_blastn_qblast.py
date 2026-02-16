# 1) Use Biopython to submit a DNA sequence to NCBI BLAST (blastn)
# and display the title and length of the top three alignments.
#
# Expected Output (example):
# 1. <alignment title> | length: <len>
# 2. <alignment title> | length: <len>
# 3. <alignment title> | length: <len>
#
# Note: Requires internet access and NCBI usage compliance.

from Bio.Blast import NCBIWWW, NCBIXML

sequence = "ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGC"

result_handle = NCBIWWW.qblast("blastn", "nt", sequence)
blast_record = NCBIXML.read(result_handle)

for i, alignment in enumerate(blast_record.alignments[:3], start=1):
    print(f"{i}. {alignment.title} | length: {alignment.length}")
