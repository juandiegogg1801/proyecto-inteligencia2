# Agente de IA para la Academia Boyacense de Historia

Este proyecto implementa un agente de IA que responde preguntas sobre la historia de Boyacá, documentos PDF, el museo de la Casa del Fundador y personajes históricos. Incluye una interfaz web para usuarios y administradores, métricas de uso y controles éticos.

## Estructura
- **backend/**: API FastAPI, agente, gestión de documentos, integración Llama 3, métricas
- **frontend/**: Interfaz web (React) con chat, administración y métricas
- **data/pdfs/**: Almacenamiento de documentos PDF

## Tecnologías
- FastAPI, React, llama.cpp, FAISS/ChromaDB, PyMuPDF

## Guía de Uso
1. Instala dependencias en `backend/` y `frontend/`.
2. Ejecuta el backend:
	```bash
	cd backend
	uvicorn main:app --reload
	```
3. Ejecuta el frontend:
	```bash
	cd frontend
	npm start
	```
4. Accede a la web para:
	- Consultar al agente IA en la sección de chat
	- Administrar documentos PDF (subir, eliminar, reindexar)
	- Visualizar métricas de uso (latencia, preguntas, respuestas)

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
