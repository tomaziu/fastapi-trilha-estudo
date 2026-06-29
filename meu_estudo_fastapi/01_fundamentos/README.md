# 01 - Fundamentos do FastAPI

## O que é

FastAPI é um framework web moderno para Python, rápido, com tipagem automática e documentação interativa (Swagger/ReDoc).

## Como funciona

1. Você define rotas com decoradores (`@app.get`, `@app.post`)
2. FastAPI extrai dados automaticamente (path, query, body)
3. Valida com Pydantic
4. Retorna JSON

## Primeira rota

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensagem": "Olá, FastAPI!"}
```

## Para rodar

```bash
uvicorn main:app --reload
```

Acesse `http://127.0.0.1:8000/docs` para ver o Swagger.

## Exercícios

- `exercicio_1.py` - Criar uma rota GET que retorna seu nome
- `exercicio_2.py` - Criar rotas GET e POST no mesmo app
- `exercicio_3.py` - Explorar o Swagger e entender a documentação automática
