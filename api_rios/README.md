## 🚀 Passo a passo

Abra o terminal (Linux/Mac) ou PowerShell (Windows) e execute:

```bash
mkdir api_rios
cd api_rios

# Criar ambiente virtual
python -m venv .venv

# Windows
venv\Scripts\activate

# Linux
source .venv/bin/activate


# Instalar FastAPI
pip install "fastapi[standard]"

# Abra o VS Code
code .


# main.py - código de exemplo
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Olá, FastAPI no IFPI - TDS 386!"}

# Rodar o Servidor
fastapi dev main.py


# Acessar Navegador
http://127.0.0.1:8000/hello

