# 7) Detect N-glycosylation motif: N[^P][ST][^P]
#
# Expected Output (example):
# Motif: NVTN at 0

import re

seq = "NVTNQSTNPATSNKS"
pattern = r"N[^P][ST][^P]"

for m in re.finditer(pattern, seq):
    print("Motif:", m.group(), "at", m.start())
