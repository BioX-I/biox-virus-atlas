from biox_virus_atlas.structure import pdb_entry_url, uniprot_url


def test_urls():
    assert pdb_entry_url("1a2k") == "https://files.rcsb.org/download/1A2K.pdb"
    assert uniprot_url("P0DTC2").endswith("P0DTC2.fasta")
