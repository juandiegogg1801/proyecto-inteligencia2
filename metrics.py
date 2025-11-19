import time
import threading
from collections import deque

# Métricas simples en memoria
METRICS = {
    'questions': deque(maxlen=1000),  # Guarda últimas 1000 consultas
}

lock = threading.Lock()

def log_question(question, answer, latency):
    with lock:
        METRICS['questions'].append({
            'question': question,
            'answer': answer,
            'latency': latency,
            'timestamp': time.time()
        })

def get_metrics():
    with lock:
        return list(METRICS['questions'])
