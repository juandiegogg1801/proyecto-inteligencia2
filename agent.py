import os
import fitz  # PyMuPDF
import faiss
import numpy as np
from typing import List

PDF_DIR = "../data/pdfs"
VECTOR_DB = "vectors.index"

# Utilidad para extraer texto de PDFs
def extract_text_from_pdfs():
    texts = []
    for filename in os.listdir(PDF_DIR):
        if filename.endswith('.pdf'):
            doc = fitz.open(os.path.join(PDF_DIR, filename))
            text = " ".join([page.get_text() for page in doc])
            texts.append((filename, text))
    return texts

# Simulación de embedding (reemplazar por modelo real)
def fake_embed(text):
    np.random.seed(hash(text) % 2**32)
    return np.random.rand(384).astype('float32')

# Indexar textos en FAISS
def build_vector_index():
    texts = extract_text_from_pdfs()
    index = faiss.IndexFlatL2(384)
    meta = []
    for filename, text in texts:
        emb = fake_embed(text)
        index.add(np.array([emb]))
        meta.append(filename)
    faiss.write_index(index, VECTOR_DB)
    with open(VECTOR_DB + '.meta', 'w') as f:
        f.write("\n".join(meta))

# Buscar en el vector store
def search_similar(query, top_k=1):
    index = faiss.read_index(VECTOR_DB)
    with open(VECTOR_DB + '.meta') as f:
        meta = f.read().splitlines()
    emb = fake_embed(query)
    D, I = index.search(np.array([emb]), top_k)
    results = []
    for idx in I[0]:
        filename = meta[idx]
        with fitz.open(os.path.join(PDF_DIR, filename)) as doc:
            text = " ".join([page.get_text() for page in doc])
        results.append((filename, text))
    return results

# Integración con Llama 3 (placeholder)
def query_llama3(question, context):
    # Aquí se debe invocar llama.cpp con el contexto y la pregunta
    return f"Respuesta generada por Llama 3 basada en: {context[:200]}..."

# Función principal del agente
def answer_question(question):
    docs = search_similar(question, top_k=1)
    context = docs[0][1] if docs else ""
    answer = query_llama3(question, context)
    return answer
