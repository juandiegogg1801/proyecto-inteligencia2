import agent

def reindex_documents():
    agent.build_vector_index()
    return "Índice de vectores reconstruido."
