#Reading FASTA File from UNIPROT
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
record=SeqIO.read("INS gene.fasta", "fasta")
print(record.id)
print(record.description)
print(record.seq)
print(len(record.seq))

insulin=str(record.seq)
freq={}

#for amino acid count in INS gene 
for aa in insulin:
        if aa in freq:
                freq[aa] += 1
        else:
                freq[aa] = 1

print("Amino acid frequency in insulin",freq)

total=len(insulin)
print("Total amino acid composition in insulin",total)

#for calculating amino acid percentage in INS gene
for aa in freq:
    percentage = (freq[aa] / total) * 100
print(aa, "=", round(percentage, 2), "%")


#for calculating molecular weight of INS gene
analysis= ProteinAnalysis(insulin)
mw=analysis.molecular_weight()
print("Molecular weight of INS",round(mw,2))

#for finding isoelectric point
pi=analysis.isoelectric_point
print("Isoelectric point",pi)

#for finding hydrophobic amino acids in INS gene
hydrophobic = "AVLIMFWYP"

hydrophobic_count = 0

for aa in insulin:
    if aa in hydrophobic:
        hydrophobic_count += 1

print("Hydrophobic Residues in INS", hydrophobic_count)
print("Hydrophobic Percentage IN INS", round((hydrophobic_count/total)*100, 2), "%")

#for finding Hydrophilic amino acids in INS gene
hydrophilic = "RNDQEKHSTCG"

hydrophilic_count = 0

for aa in insulin:
    if aa in hydrophilic:
        hydrophilic_count += 1

print("Hydrophilic Residues in INS", hydrophilic_count)
print("Hydrophilic Percentage in INS", round((hydrophilic_count/total)*100, 2), "%")

# Store INS values for comparison
hydrophobic_ins = hydrophobic_count
hydrophilic_ins = hydrophilic_count

mw_ins = mw
pi_ins = pi

freq_ins = freq.copy()
total_ins = total

records=SeqIO.read("GCG gene.fasta", "fasta")
print("protein id", records.id)
print("protein description", records.description)
print("protein seq", records.seq)
print("protein seq length",len(records.seq))

glucagon=str(records.seq)
freq={}

#For amino acid count in GCG
for aa in glucagon:
      if aa in freq:
            freq[aa] += 1
      else:
            freq[aa] = 1
print("Amino acid frequency in GCG", freq)

total=len(glucagon)
print("Total amino acid composition in GCG", total)

#For calculating amino acid percentage
for aa in freq:
      percentage=(freq[aa]/total)*100
print(aa,"=",round(percentage,2),"%")

#for calculating molecular weight in GCG
analysis=ProteinAnalysis(glucagon)
mw=analysis.molecular_weight()
print("Molecular weight of GCG",(round(mw,2)))

#for finding isoelectric point
pi=analysis.isoelectric_point()
print("Isoelctic point", pi)

#for finding hydrophobic amino acids in GCG gene
hydrophobic = "AVLIMFWYP"
hydrophilic_count=0
for aa in glucagon:
      if aa in hydrophobic:
            hydrophobic_count += 1
print("Hydrophobic residues in GCG",hydrophobic_count)
print("Hydrophobic percentage in GCG", (round(hydrophobic_count/total)*100,2,"%"))

#for finding hydrophilic amino acids in GCG gene
hydrophilic = "RNDQEKHSTCG"
for aa in glucagon:
      if aa in hydrophilic:
            hydrophilic_count += 1
print("Hydrophilic residues in GCG", hydrophilic_count)
print("Hydrophilic percentage in GCG", (round(hydrophilic_count/total)*100,2,"%"))

#Storing GCG values for comparison
hydrophobic_gcg = hydrophobic_count
hydrophilic_gcg = hydrophilic_count

mw_gcg = mw
pi_gcg = pi

freq_gcg = freq.copy()
total_gcg = total

#for plotting bar plot for comparing between insulin(INS) and glucagon(GCG) genes
import matplotlib.pyplot as plt
import numpy as np

# Protein names
proteins = ["INS", "GCG"]

# X-axis positions
x = np.arange(len(proteins))

# Width of each bar
width = 0.35

# Data
hydrophobic = [hydrophobic_ins, hydrophobic_gcg]
hydrophilic = [hydrophilic_ins, hydrophilic_gcg]

#for creating figure
plt.figure(figsize=(6,5))
plt.bar(x - width/2, hydrophobic, width, label="Hydrophobic Residues", color="Pink")
plt.bar(x + width/2, hydrophilic, width, label="Hydrophilic Residues", color="Blue")

#for adding labels and title
plt.title("Comparison of Hydrophobic and Hydrophilic Residues")
plt.xlabel("Proteins")
plt.ylabel("Number of Residues")

#for showing INS and GCG on x-axis
plt.xticks(x, proteins)

plt.show()

# for plotting a bar graph to compare molecular weights of INS and GCG
import matplotlib.pyplot as plt
import numpy as np
proteins=["INS","GCG"]
molecular_weight=[mw_ins,mw_gcg]
plt.bar(proteins, molecular_weight, color="Lightgreen")
plt.title("Comparison of molecular weight")
plt.xlabel("Proteins")
plt.ylabel("Molecular weight(Da)")

plt.show()

