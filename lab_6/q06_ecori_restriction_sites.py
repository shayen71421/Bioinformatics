# 6) Identify all EcoRI restriction sites (GAATTC) using regex.
#
# Expected Output (example):
# EcoRI site at position: 2
# EcoRI site at position: 10
# EcoRI site at position: 20

import re

seq = "AAGAATTCTTGAATTCCAAGGAATTC"
pattern = r"GAATTC"

for m in re.finditer(pattern, seq):
    print("EcoRI site at position:", m.start())
