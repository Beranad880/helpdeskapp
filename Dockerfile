# ==========================================
# Fáze 1: Sestavení frontendu (Vue 3 + Vite)
# ==========================================
FROM node:18-slim AS frontend-builder
WORKDIR /frontend

# Instalace závislostí frontendu
COPY frontend/package*.json ./
RUN npm install

# Sestavení produkčního balíčku
COPY frontend/ .
RUN npm run build

# ==========================================
# Fáze 2: Finální produkční Python kontejner
# ==========================================
FROM python:3.9-slim
WORKDIR /app

# Instalace závislostí backendu
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Zkopírování backendového kódu
COPY backend/ .

# Zkopírování zkompilovaného frontendu z 1. fáze do složky dist/
COPY --from=frontend-builder /frontend/dist ./dist

# Spuštění Uvicornu na portu poskytnutém Railway (nebo default 8080)
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]
