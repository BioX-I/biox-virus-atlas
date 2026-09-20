"""IO NCBI : fetch minimal via Entrez (Biopython), avec cache local."""
from pathlib import Path


def fetch_genbank(accessions: list[str], out_dir: str | Path, email: str) -> list[Path]:
    from Bio import Entrez
    Entrez.email = email
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for acc in accessions:
        target = out / f"{acc}.gb"
        if target.exists():
            written.append(target)
            continue
        with Entrez.efetch(db="nucleotide", id=acc, rettype="gb", retmode="text") as handle:
            target.write_text(handle.read(), encoding="utf-8")
        written.append(target)
    return written
