# Hantavirus — fiche generale (in silico uniquement)

## C'est quoi ?

Famille `Hantaviridae` (ordre Bunyavirales). Virus a ARN tri-segmentes (S, M, L).
Reservoir naturel : rongeurs (selon espece : campagnols, mulots, rats, souris).
Transmission : aerosol d'excretas de rongeurs, pas de transmission interhumaine en general pour les formes europeennes.

## Deux tableaux cliniques (niveau general)

- Vieux Monde (ex : Puumala, Dobrava, Hantaan) : fievre hemorragique a syndrome renal (FHSR), gravite variable.
- Nouveau Monde (ex : Sin Nombre, Andes) : syndrome cardio-pulmonaire (SCPH), plus severe.

En Europe de l'Ouest : surtout Puumala (nephropathia epidemica, forme souvent moderee).

## Pourquoi c'est un bon cas d'etude bio+dev ?

- Diversite genomique + phylogeographie (lien rongeur / region).
- Segments S/M/L : bon exercice de QC, alignement, phylogenie.
- Structures publiques (nucleoproteine, glycoproteines d'enveloppe) pour le volet v0.2.
- Donnees publiques abondantes sur NCBI, sans jamais manipuler d'agent reel.

## Ce qu'on fait ici (et ce qu'on ne fait pas)

Fait : fetch public NCBI, QC FASTA, alignement, arbre, mapping PDB/UniProt, notebooks reproductibles.
Ne fait pas : culture, isolement, manipulation d'echantillon, protocole humide. 100% in silico.

## Premier MVP (v0.1)

1. Choisir 1 espece focus (propose : Puumala, europeen, bien documente).
2. 10 genomes segment S publics -> `data/raw/` (gitignored).
3. QC + alignement + arbre test.
4. Notebook 01 + tag v0.1.0.

References : voir `docs/REFERENCES.md` (NCBI Virus, PDB, UniProt, Nextstrain).
