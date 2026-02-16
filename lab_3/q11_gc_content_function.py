# Q11. Write a function to calculate GC%.
#
# Expected Output:
# 66.66666666666666


def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100

print(gc_content("ATGCGC"))
