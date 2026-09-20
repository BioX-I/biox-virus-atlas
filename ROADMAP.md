# ROADMAP — biox-virus-atlas (PUBLIC)

Vision : atlas open-source pour explorer les virus via donnees publiques : genomes + structures + phylogenie.

## v0.1.0 — MVP genomique

- [ ] Fetch NCBI Virus (ex : 10 genomes, 1 espece test)
- [ ] Parse FASTA, QC longueur / N
- [ ] BLAST / alignement + arbre phylo (MEGA / IQ-TREE ou Biopython)
- [ ] Notebook 01 reproductible
- [ ] Tests >=80%, CI verte
- [ ] Tag `v0.1.0`

## v0.2.0 — + Structure

- [ ] Fetch PDB / UniProt pour 1-2 proteines cibles
- [ ] Mapping genome -> proteine, visualisation 3D (notebook)
- [ ] Tests structure, docs references

## v0.3.0 — Veille (optionnel)

- [ ] Dashboard variants (Nextstrain-like simplifie)
- [ ] Export figures pour papier

## Install

```bash
pip install -r requirements.txt
pytest -q
```

Licence MIT.
