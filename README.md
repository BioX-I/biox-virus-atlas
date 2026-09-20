# biox-virus-atlas

Atlas genomique + structure virale. Partie de l'ecosysteme BioX (`BioX-I`).
Scope MVP : genomique (NCBI, FASTA, BLAST, phylogenie) + structure (PDB, UniProt).

Profil : bio + dev. 100% in silico, donnees publiques uniquement.

## Quick start

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
```

## Structure

```
src/biox_virus_atlas/  # code (genomics, structure, io_ncbi)
tests/                 # pytest, >=80% (R102)
notebooks/             # exploration
data/                  # raw (gitignored) + README
docs/                  # references publiques
ROADMAP.md             # public (tracked)
PLAN.md                # prive (gitignored, R106)
```

## Ecosysteme (R105)

- Hub : `Documents/BioX/` voir `ECOSYSTEM_MAP.md` et `COMPATIBILITY_MATRIX.md`
- Aucune interface partagee pour l'instant.

## Licence

MIT. Donnees : respecter les termes NCBI / PDB / UniProt. Pas d'agent pathogen reel, in silico uniquement.
