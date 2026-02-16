# 4) Use Bio.Align PairwiseAligner to align two DNA sequences
# and display the best alignment.
#
# Expected Output (example):
# score = <score>
# <alignment>

from Bio.Align import PairwiseAligner

seq1 = "ATGCGTAC"
seq2 = "ATGACGTAC"

aligner = PairwiseAligner()
alignments = aligner.align(seq1, seq2)
best = alignments[0]

print("score =", best.score)
print(best)
