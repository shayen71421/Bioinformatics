# 5) Find all occurrences of the TATA box (TATA[AT]A) using regex.
#
# Expected Output (example):
# [(3, 'TATATA'), (14, 'TATATA')]

import re

seq = "ACGTATATAAACGTTATATAAATATAAGG"
pattern = r"TATA[AT]A"

matches = [(m.start(), m.group()) for m in re.finditer(pattern, seq)]
print(matches)
