# 12) Read file until an unknown base (N) is found
#
# Expected Output (example):
# Valid sequence: ATGCGT
# Valid sequence: AATTGG
# Unknown base found, stopping!

with open("dna_list.txt") as f:
    for line in f:
        seq = line.strip().upper()
        if "N" in seq:
            print("Unknown base found, stopping!")
            break
        print("Valid sequence:", seq)
