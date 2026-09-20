"""Visuels simples : QC 10 S Puumala + schema genome 3 segments."""
import sys
sys.path.insert(0, "src")
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from biox_virus_atlas.genomics import parse_fasta, qc_stats

seqs = parse_fasta("data/raw/puumala_S_10.fasta")
q = qc_stats(seqs)
names = list(q.keys())
lengths = [q[k]["length"] for k in names]
gcs = [q[k]["gc"] for k in names]
short = [n.split(".")[0] for n in names]

# 1. Longueurs + GC
fig, axes = plt.subplots(2, 1, figsize=(10, 6))
axes[0].bar(short, lengths)
axes[0].set_title("Puumala S - longueur (nt) - 10 genomes")
axes[0].tick_params(axis="x", rotation=30)
axes[1].bar(short, gcs)
axes[1].set_title("Puumala S - GC fraction")
axes[1].tick_params(axis="x", rotation=30)
fig.tight_layout()
Path("docs/figures").mkdir(parents=True, exist_ok=True)
fig.savefig("docs/figures/qc_puumala_S.png", dpi=150)
print("OK qc_puumala_S.png", len(names))

# 2. Schema genome 3 segments (tailles typiques)
fig2, ax = plt.subplots(figsize=(10, 2.5))
segs = [("S ~1.8 kb\nnucleoproteine", 1.8), ("M ~3.6 kb\nglycoproteines", 3.6), ("L ~6.5 kb\npolymerase", 6.5)]
x = 0
for label, size in segs:
    ax.barh(0, size, left=x, height=0.4)
    ax.text(x + size / 2, 0, label, ha="center", va="center", fontsize=9)
    x += size + 0.3
ax.set_xlim(0, x)
ax.set_title("Hantavirus - genome en 3 segments ARN (1 virus = S + M + L)")
ax.set_xlabel("taille (kb)")
ax.set_yticks([])
fig2.tight_layout()
fig2.savefig("docs/figures/genome_3_segments.png", dpi=150)
print("OK genome_3_segments.png")
