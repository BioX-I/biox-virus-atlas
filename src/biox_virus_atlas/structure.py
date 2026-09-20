"""Structure : helpers PDB/UniProt (fetch simple, pas de parsing lourd au MVP)."""
import requests


def pdb_entry_url(pdb_id: str) -> str:
    return f"https://files.rcsb.org/download/{pdb_id.upper()}.pdb"


def uniprot_url(accession: str) -> str:
    return f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"


def fetch_text(url: str, timeout: int = 30) -> str:
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    return r.text
