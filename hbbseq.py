from Bio import SeqIO
record=SeqIO.read("hbbseq.fasta", "fasta")
print(record.id)
print(record.description)
print(len(record))
print(record.seq)

for seq_record in SeqIO.parse("hbbseq.fasta", "fasta"):
    seq=str(seq_record.seq)
    g_count=seq.count("G")
    c_count=seq.count("C")
    gc_count=(seq.count("G")+seq.count("C"))/len(seq)*100

    a_count=seq.count("A")
    t_count=seq.count("T")
    at_count=(seq.count("A")+seq.count("T"))/len(seq)*100

print(g_count)
print(c_count)
print(gc_count)
print(a_count)
print(t_count)
print(at_count)