# 3) Use Biopython PDB module to parse a PDB file and extract structure info.
#
# Expected Output (example):
# Structure ID: 1ABC
# Models: 1
# Chains: 2
# Residues: 150

from Bio.PDB import PDBParser

pdb_file = "example.pdb"
parser = PDBParser(QUIET=True)
structure = parser.get_structure("structure", pdb_file)

model_count = 0
chain_count = 0
residue_count = 0

for model in structure:
    model_count += 1
    for chain in model:
        chain_count += 1
        for residue in chain:
            residue_count += 1

print("Structure ID:", structure.id)
print("Models:", model_count)
print("Chains:", chain_count)
print("Residues:", residue_count)
