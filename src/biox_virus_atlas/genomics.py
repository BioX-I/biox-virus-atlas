"""Genomique de base : parse FASTA + stats QC (KISS, sans dependance lourde)."""
from pathlib import Path


def parse_fasta(path: str | Path) -> dict[str, str]:
    seqs: dict[str, str] = {}
    header: str | None = None
    chunks: list[str] = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    seqs[header] = "".join(chunks).upper()
                header = line[1:].split()[0]
                chunks = []
            else:
                chunks.append(line)
    if header is not None:
        seqs[header] = "".join(chunks).upper()
    return seqs


def gc_content(seq: str) -> float:
    seq = seq.upper()
    if not seq:
        return 0.0
    gc = sum(1 for b in seq if b in ("G", "C"))
    return gc / len(seq)


def qc_stats(seqs: dict[str, str]) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for name, seq in seqs.items():
        out[name] = {
            "length": float(len(seq)),
            "gc": gc_content(seq),
            "n_frac": seq.count("N") / len(seq) if seq else 0.0,
        }
    return out
