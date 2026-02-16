# Q15. Write GC% to a file.
#
# Expected Output:
# Creates gc_output.txt with the GC% value


def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100

f = open("seq.fasta")
lines = f.readlines()
seq = "".join(line.strip() for line in lines if not line.startswith(">"))

gc = gc_content(seq)
with open("gc_output.txt", "w") as out:
    out.write(str(gc))
