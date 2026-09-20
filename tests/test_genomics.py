from biox_virus_atlas.genomics import gc_content, parse_fasta, qc_stats


def test_parse_and_qc(tmp_path):
    f = tmp_path / "t.fasta"
    f.write_text(">a\nATGCN\n>b\nGGCC\n", encoding="utf-8")
    seqs = parse_fasta(f)
    assert seqs == {"a": "ATGCN", "b": "GGCC"}
    assert gc_content("GGCC") == 1.0
    stats = qc_stats(seqs)
    assert stats["a"]["length"] == 5.0
    assert stats["b"]["gc"] == 1.0
