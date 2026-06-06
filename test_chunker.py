from core.text_chunker import chunk_text

def test_chunk_text():
    text = "Paragraph 1\n\nParagraph 2\n\nParagraph 3"
    # force small max_chars to test splitting
    chunks = chunk_text(text, max_chars=12)
    assert len(chunks) == 3
    assert chunks[0] == "Paragraph 1"
    assert chunks[1] == "Paragraph 2"
    assert chunks[2] == "Paragraph 3"
    
def test_chunk_text_combine():
    text = "Paragraph 1\n\nParagraph 2\n\nParagraph 3"
    # allow combining two paragraphs (len is 11 + 2 + 11 = 24)
    chunks = chunk_text(text, max_chars=30)
    assert len(chunks) == 2
    assert chunks[0] == "Paragraph 1\n\nParagraph 2"
    assert chunks[1] == "Paragraph 3"
