#!/bin/bash

# Usa el puerto que Render inyecta, o 8000 si no está definido (para local)
PORT=${PORT:-8000}

uvicorn main:app --host 0.0.0.0 --port $PORT
