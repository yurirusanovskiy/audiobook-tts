import re
from typing import List
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

# Global instance to avoid reloading the model on every call
_embeddings_instance = None

def get_embeddings():
    global _embeddings_instance
    if _embeddings_instance is None:
        import os
        # Use a persistent local cache directory to prevent macOS from deleting the temp ONNX files
        cache_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models', 'fastembed_cache'))
        os.makedirs(cache_dir, exist_ok=True)
        # Using a lightweight, fast, multilingual model suitable for Russian
        _embeddings_instance = FastEmbedEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
            cache_dir=cache_dir
        )
    return _embeddings_instance

def chunk_text_semantically(text: str, max_chars: int = 7000) -> List[str]:
    """
    Chunks a large text semantically using local embeddings.
    It groups sentences by topic and creates boundaries where the narrative shifts,
    while trying to keep chunks under max_chars.
    """
    if not text.strip():
        return []

    try:
        embeddings = get_embeddings()
        
        # The SemanticChunker splits by sentences and compares their cosine similarity.
        # It sets a breakpoint where the semantic difference is highest (e.g. above a percentile).
        text_splitter = SemanticChunker(embeddings, breakpoint_threshold_type="percentile")
        docs = text_splitter.create_documents([text])
        semantic_groups = [doc.page_content.strip() for doc in docs if doc.page_content.strip()]
    except Exception as e:
        # Fallback to simple chunking if ML chunking or model initialization fails for some reason
        print(f"ML Chunking failed: {e}. Falling back to basic paragraph chunking.")
        return fallback_chunk_text(text, max_chars)
    
    # Pack semantic groups into chunks that fit the max_chars constraint
    final_chunks = []
    current_chunk = []
    current_length = 0
    
    for group in semantic_groups:
        # If adding this group exceeds the limit and we have content
        if current_length + len(group) > max_chars and current_chunk:
            final_chunks.append("\n\n".join(current_chunk))
            current_chunk = [group]
            current_length = len(group)
        else:
            current_chunk.append(group)
            current_length += len(group) + 2 # +2 for \n\n
            
    if current_chunk:
        final_chunks.append("\n\n".join(current_chunk))
        
    return final_chunks

def fallback_chunk_text(text: str, max_chars: int = 7000) -> List[str]:
    """Simple paragraph-based chunker as a fallback."""
    paragraphs = re.split(r'\n\s*\n', text)
    chunks = []
    current_chunk = []
    current_length = 0
    
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if current_length + len(p) > max_chars and current_chunk:
            chunks.append("\n\n".join(current_chunk))
            current_chunk = [p]
            current_length = len(p)
        else:
            current_chunk.append(p)
            current_length += len(p)
            
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))
        
    return chunks
