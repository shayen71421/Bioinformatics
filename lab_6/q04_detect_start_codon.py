# 4) Identify all occurrences of the start codon (ATG) using regex.
#
# Expected Output (example):
# Start codon at position: 0
# Start codon at position: 14
# Start codon at position: 28

import re
from Bio.Seq import Seq

seq = "ATGCGTACGTTAAGATGCCCGGATAGCCATGTTA"
pattern = r"ATG"

for m in re.finditer(pattern, seq):
    print("Start codon at position:", m.start())
