# 14) Transcribe DNA to RNA by replacing T with U
#
# Expected Output:
# RNA: ACGGCCGGUUCCAAUUGC


def transcribe(seq):
    return seq.replace("T", "U")


dna = "ACGGCCGGTTCCAATTGC"
rna = transcribe(dna)
print("RNA:", rna)
