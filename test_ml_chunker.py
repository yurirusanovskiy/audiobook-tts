from core.ml_text_chunker import chunk_text_semantically

def test_ml_chunker():
    # Long text with different topics
    text = (
        "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do. "
        "Once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it. "
        "And what is the use of a book, thought Alice without pictures or conversation? \n\n"
        "Suddenly a White Rabbit with pink eyes ran close by her. "
        "There was nothing so VERY remarkable in that; nor did Alice think it so VERY much out of the way to hear the Rabbit say to itself, 'Oh dear! Oh dear! I shall be late!' "
        "But when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-POCKET, and looked at it, and then hurried on, Alice started to her feet. \n\n"
        "In another moment down went Alice after it, never once considering how in the world she was to get out again. "
        "The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down. "
    )
    
    # We set a low max_chars to force it to split semantic groups
    chunks = chunk_text_semantically(text, max_chars=400)
    print("Chunks created:", len(chunks))
    for i, c in enumerate(chunks):
        print(f"--- Chunk {i+1} ({len(c)} chars) ---")
        print(c)
        
    assert len(chunks) > 1

if __name__ == "__main__":
    test_ml_chunker()
