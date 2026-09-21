"""Detecteur de liens entre virus par k-mers (le 'langage' = vocabulaire de k-mers).
Arbre = dendrogramme de similarite k-mer (MVP, pas une phylogenie MSA/IQ-TREE).
Predictor safe : plus proches voisins par similarite, jamais de prediction de danger.
"""
import sys
sys.path.insert(0, "src")
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
from biox_virus_atlas.genomics import parse_fasta

K = 6
FASTA = Path("data/raw/puumala_S_10.fasta")
FIG = Path("docs/figures")
FIG.mkdir(parents=True, exist_ok=True)

def kmer_vocab(k=K):
    from itertools import product
    return {"".join(p): i for i, p in enumerate(product("ACGT", repeat=k))}

VOCAB = kmer_vocab()
DIM = len(VOCAB)

def kmer_vector(seq: str) -> np.ndarray:
    seq = seq.upper()
    v = np.zeros(DIM, dtype=np.float32)
    for i in range(len(seq) - K + 1):
        kmer = seq[i:i + K]
        j = VOCAB.get(kmer)
        if j is not None:
            v[j] += 1
    s = v.sum()
    return v / s if s else v

seqs = parse_fasta(FASTA)
names = list(seqs.keys())
short = [n.split(".")[0] for n in names]
X = np.stack([kmer_vector(seqs[n]) for n in names])

# Cosine distance
D = squareform(pdist(X, metric="cosine"))
sim = 1 - D

# Liens : similarite > seuil
THR = 0.90
edges = [(names[i], names[j], float(sim[i, j]))
         for i in range(len(names)) for j in range(i + 1, len(names))
         if sim[i, j] >= THR]
print(f"Sequences: {len(names)}, K={K}, seuil lien={THR}")
print(f"Liens detectes: {len(edges)}/{len(names)*(len(names)-1)//2}")
for a, b, s in sorted(edges, key=lambda e: -e[2])[:15]:
    print(f"  {a.split('.')[0]} <-> {b.split('.')[0]}  sim={s:.4f}")

# Heatmap similarite
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(sim, vmin=0.5, vmax=1.0)
ax.set_xticks(range(len(short)), short, rotation=45, ha="right", fontsize=8)
ax.set_yticks(range(len(short)), short, fontsize=8)
ax.set_title("Puumala S - similarite k-mer (cosine, K=6) = detecteur de liens")
fig.colorbar(im, label="similarite")
fig.tight_layout()
fig.savefig(FIG / "links_heatmap_puumala_S.png", dpi=150)

# Arbre (dendrogramme average sur distance cosine)
Z = linkage(pdist(X, metric="cosine"), method="average")
fig2, ax2 = plt.subplots(figsize=(8, 5))
dendrogram(Z, labels=short, ax=ax2)
ax2.set_title("Puumala S - arbre de similarite k-mer (MVP, pas IQ-TREE)")
ax2.tick_params(axis="x", rotation=30, labelsize=8)
fig2.tight_layout()
fig2.savefig(FIG / "tree_kmer_puumala_S.png", dpi=150)
print("OK figures: links_heatmap + tree_kmer")

# Demo predicteur : sequence test = seq0 avec 5 mutations
rng = np.random.default_rng(0)
s0 = seqs[names[0]]
lst = list(s0)
for pos in rng.choice(len(lst), 5, replace=False):
    lst[pos] = rng.choice([b for b in "ACGT" if b != lst[pos]])
test_seq = "".join(lst)
tv = kmer_vector(test_seq)
sims = (X / (np.linalg.norm(X, axis=1, keepdims=True) + 1e-9)) @ (tv / (np.linalg.norm(tv) + 1e-9))
top = np.argsort(-sims)[:3]
print("Demo predicteur (seq test = seq0 + 5 mutations):")
for j in top:
    print(f"  {names[j]} sim={float(sims[j]):.4f}")
