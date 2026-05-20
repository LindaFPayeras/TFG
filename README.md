# TFG

Proyecto de asistente conversacional para apoyo emocional, con interfaz para pacientes y terapeutas.

## Objetivo

- Permitir que un paciente converse con un asistente IA.
- Clasificar la emocion del mensaje del paciente.
- Guardar el historial de conversacion.
- Generar reportes/resumenes para terapeutas.
- Mostrar una interfaz web sencilla con Streamlit.

## Estructura

```text
TFG/
+-- backend/
|   +-- main.py
|   +-- routes/
|   +-- models/
|   +-- services/
|       +-- auth_service/
|       +-- chat_service/
|       +-- data_service/
|       +-- summary_service/
+-- front_service/
|   +-- streamlit.py
|   +-- functions.py
|   +-- static/
+-- main.py
+-- requirements.txt
+-- README.md
```

## Tecnologias

- Python
- FastAPI
- Streamlit
- Ollama
- Transformers
- Torch
- Pydantic
- Requests

## Instalacion

Crear entorno virtual:

```bash
python -m venv .venv
```

Activar entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecucion completa

El archivo `main.py` permite lanzar backend y frontend a la vez.

```bash
python main.py
```

Este script:

- Inicia el backend con Uvicorn en el puerto `1350`.
- Inicia el frontend con Streamlit.
- Abre la aplicacion en `http://localhost:8501`.

## Backend

API desarrollada con FastAPI.

Endpoints principales:

- `POST /auth/login`: login de usuario.
- `POST /chat`: envia un mensaje al asistente.
- `GET /data/{user_id}`: obtiene el historial de un paciente.
- `GET /report/{user_id}`: genera el resumen de un paciente.
- `GET /data/relation/{therapist_id}`: obtiene los pacientes de un terapeuta.

Ejecutar backend:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 1350
```

## Frontend

Interfaz desarrollada con Streamlit.

Funcionalidades:

- Login de paciente o terapeuta.
- Chat para pacientes.
- Vista de pacientes para terapeutas.
- Reporte/resumen del historial de cada paciente.

Ejecutar frontend:

```bash
streamlit run front_service/streamlit.py
```

## Configuracion

El frontend espera una variable `API_URL` en `front_service/config.py`.

Ejemplo:

```python
API_URL = "http://localhost:1350"
```

Tambien es necesario tener Ollama disponible con el modelo usado por el backend:

```bash
ollama pull llama3
```

## Datos

Los datos se guardan en ficheros JSON:

- Usuarios: `backend/services/auth_service/users.json`
- Historiales: `backend/services/data_service/data/history/`
- Relaciones terapeuta-paciente: `backend/services/data_service/data/relations/therapist-user.json`

## Notas

- El proyecto usa almacenamiento local en JSON.
- Algunas metricas del frontend estan marcadas como mock.
- Las dependencias principales estan definidas en `requirements.txt`.
