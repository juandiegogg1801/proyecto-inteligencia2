from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
import os
from agent import answer_question
from document_manager import reindex_documents
from metrics import log_question, get_metrics

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto a ['http://localhost:3000']
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
security = HTTPBasic()
PDF_DIR = "../data/pdfs"
ADMIN_USER = "admin"
ADMIN_PASS = "admin123"  # Cambia esto en producción

# Autenticación básica para admin
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != ADMIN_USER or credentials.password != ADMIN_PASS:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return True

@app.get("/")
def root():
    return {"message": "Agente IA Academia Boyacense de Historia"}

@app.post("/admin/upload_pdf")
def upload_pdf(file: UploadFile = File(...), auth: bool = Depends(authenticate)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF")
    file_path = os.path.join(PDF_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return {"message": f"PDF {file.filename} subido exitosamente"}

@app.delete("/admin/delete_pdf/{filename}")
def delete_pdf(filename: str, auth: bool = Depends(authenticate)):
    file_path = os.path.join(PDF_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    os.remove(file_path)
    return {"message": f"PDF {filename} eliminado"}

@app.get("/admin/list_pdfs")
def list_pdfs(auth: bool = Depends(authenticate)):
    files = [f for f in os.listdir(PDF_DIR) if f.endswith('.pdf')]
    return {"pdfs": files}

# Endpoint para preguntas (placeholder)
from pydantic import BaseModel

class AskRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(req: AskRequest):
    import time
    start = time.time()
    answer = answer_question(req.question)
    latency = time.time() - start
    log_question(req.question, answer, latency)
    return {"answer": answer, "latency": latency}
# Endpoint para reindexar documentos (admin)
@app.post("/admin/reindex")
def reindex(auth: bool = Depends(authenticate)):
    msg = reindex_documents()
    return {"message": msg}

# Endpoint para consultar métricas
@app.get("/admin/metrics")
def metrics(auth: bool = Depends(authenticate)):
    return {"metrics": get_metrics()}

# Endpoint para reindexar documentos (admin)
@app.post("/admin/reindex")
def reindex(auth: bool = Depends(authenticate)):
    msg = reindex_documents()
    return {"message": msg}
