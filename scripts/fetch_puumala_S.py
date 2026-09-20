"""Fetch 10 Puumala S segment complets (FASTA) vers data/raw/ + log accessions."""
from pathlib import Path
from Bio import Entrez, SeqIO

Entrez.email = "Lemniscate_zero@proton.me"
OUT = Path("data/raw")
OUT.mkdir(parents=True, exist_ok=True)

TERM = "Orthohantavirus puumalaense[Organism] AND S segment complete sequence"
N = 10

h = Entrez.esearch(db="nucleotide", term=TERM, retmax=N, sort="relevance")
rec = Entrez.read(h)
ids = rec["IdList"]
print(f"Count total: {rec['Count']}, fetch: {len(ids)}")

summ = Entrez.read(Entrez.esummary(db="nucleotide", id=",".join(ids)))
accs = [d["AccessionVersion"] for d in summ]
print("Accessions:", accs)
(Path("data/raw") / "puumala_S_accessions.txt").write_text("\n".join(accs) + "\n", encoding="utf-8")

with Entrez.efetch(db="nucleotide", id=",".join(ids), rettype="fasta", retmode="text") as handle:
    fasta_text = handle.read()
(Path("data/raw") / "puumala_S_10.fasta").write_text(fasta_text, encoding="utf-8")

seqs = list(SeqIO.parse(OUT / "puumala_S_10.fasta", "fasta"))
print(f"Sequences ecrites: {len(seqs)}, longueurs: {[len(s.seq) for s in seqs][:5]}")
