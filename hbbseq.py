from Bio import SeqIO
record=SeqIO.read("hbbseq.fasta", "fasta")
print(record.id)
print(record.description)
print(len(record))
print(record.seq)

#parsing the FASTA file
for seq_record in SeqIO.parse("hbbseq.fasta", "fasta"):
    seq=str(seq_record.seq)
    
    a_count=seq.count("A")
    t_count=seq.count("T")
    at_count_percentage=(seq.count("A")+seq.count("T"))/len(seq)*100

    g_count=seq.count("G")
    c_count=seq.count("C")
    gc_count_percentage=(seq.count("G")+seq.count("C"))/len(seq)*100


print(a_count)
print(t_count)
print(at_count_percentage)
print(g_count)
print(c_count)
print(gc_count_percentage)

# for creating pie chart
import matplotlib.pyplot as plt
import numpy as np


bases = ["Adenine", "Thymine", "Guanine", "Cytosine"]


composition = [22068, 22309, 14785, 14146]


colors = ["Pink", "Cyan", "Lightgreen", "Orange"]


plt.pie(composition,
        labels=bases,
        colors=colors,
        autopct="%1.1f%%",
        startangle=90)


plt.title("Composition of Nitrogenous Bases")

plt.show()
plt.title("Composition of Nitrogenous Bases")

plt.show()
