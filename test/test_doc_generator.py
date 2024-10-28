from pathlib import Path

from src.doc_generator import generate_doc


def test_doc_generator():
    doc = generate_doc("", "")
    assert doc == Path(
        "test/resources/doc_generator_output_reference.md"
    ).read_text()
