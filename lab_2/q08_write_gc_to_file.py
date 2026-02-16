# 8) Write GC Content Results to a File
#
# Expected Output:
# Creates gc_summary.csv with columns: ID,GC%

with open("input.fasta") as f, open("gc_summary.csv", "w") as out:
    out.write("ID,GC%\n")
    seq_id = ""
    seq_data = ""

    for line in f:
        line = line.strip()
        if line.startswith(">"):
            if seq_id:
                gc = (seq_data.count("G") + seq_data.count("C")) / len(seq_data) * 100
                out.write(f"{seq_id},{gc:.2f}\n")
            seq_id = line[1:]
            seq_data = ""
        else:
            seq_data += line

    if seq_id:
        gc = (seq_data.count("G") + seq_data.count("C")) / len(seq_data) * 100
        out.write(f"{seq_id},{gc:.2f}\n")
