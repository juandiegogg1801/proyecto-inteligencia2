# Agente de IA para la Academia Boyacense de Historia

Este proyecto implementa un agente de IA que responde preguntas sobre la historia de Boyacá, documentos PDF, el museo de la Casa del Fundador y personajes históricos. Incluye una interfaz web para usuarios y administradores, métricas de uso y controles éticos.

## Estructura
- **backend/**: API FastAPI, agente, gestión de documentos, integración Llama 3, métricas
- **frontend/**: Interfaz web (React) con chat, administración y métricas
- **data/pdfs/**: Almacenamiento de documentos PDF

## Tecnologías
- FastAPI, React, llama.cpp, FAISS/ChromaDB, PyMuPDF

## Guía Detallada de Ejecución

### 1. Clona el repositorio
```bash
git clone https://github.com/juandiegogg1801/proyecto-inteligencia2.git
cd proyecto-inteligencia2
```

### 2. Instala dependencias

#### Backend (Python)
Requiere Python 3.12 y pip:
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Frontend (Node.js)
Requiere Node.js y npm:
```bash
cd frontend
npm install
```

### 3. Ejecuta el backend
```bash
cd backend
source .venv/bin/activate
uvicorn main:app --reload
```
El backend estará disponible en http://localhost:8000

### 4. Ejecuta el frontend
```bash
cd frontend
npm start
```
El frontend estará disponible en http://localhost:3000

### 5. Uso de la aplicación
- Accede a http://localhost:3000 en tu navegador.
- Sección "Consulta Histórica": realiza preguntas al agente.
- Sección "Panel de Administración": sube/elimina PDFs, reindexa documentos (usuario: `admin`, contraseña: `admin123`).
- Sección "Métricas de Uso": visualiza historial de preguntas y latencia.

### 6. Solución de problemas comunes
- Si ves errores de conexión, asegúrate de que ambos servidores (backend y frontend) estén corriendo.
- Si el backend no responde, revisa que el entorno virtual esté activado y las dependencias instaladas.
- Si la carpeta `node_modules` aparece en GitHub, elimina su seguimiento con:
  ```bash
  git rm -r --cached node_modules frontend/node_modules
  git commit -m "Eliminar node_modules del repositorio"
  git push
  ```

### 7. Personalización
- Puedes agregar más PDFs en `data/pdfs/` y reindexar desde el panel de administración.
- Para cambiar credenciales de admin, edita `backend/main.py`.

## Ejemplo de Pregunta
> ¿Quién fue Simón Bolívar?

## Recomendaciones Éticas y de Gobernanza
- No almacenar datos personales de los usuarios.
- Auditar y eliminar información sensible desde el panel de administración.
- Mostrar la fuente de la información cuando sea posible.
- Actualizar y reentrenar el agente con nuevos documentos de forma controlada.

## Métricas y Auditoría
- Latencia de respuesta por consulta
- Historial de preguntas y respuestas
- Visualización en tablas y gráficos

## Contacto y Contribución
Para sugerencias, mejoras o reportes, contactar a la Academia Boyacense de Historia.
