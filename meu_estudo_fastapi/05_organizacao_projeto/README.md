# 05 - Organização do Projeto (Routers)

## Por que usar routers?

Separar rotas em arquivos diferentes para manter o código organizado.

## Estrutura

```
projeto/
├── main.py
├── routers/
│   ├── clientes.py
│   ├── pedidos.py
│   └── auth.py
├── models/
│   └── schemas.py
└── database.py
```

## Exemplo

### routers/clientes.py
```python
from fastapi import APIRouter

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
def listar():
    return []

@router.post("/")
def criar():
    return {"mensagem": "Criado"}
```

### main.py
```python
from fastapi import FastAPI
from routers import clientes, pedidos

app = FastAPI()
app.include_router(clientes.router)
app.include_router(pedidos.router)
```

## Exercícios

- `exercicio_1.py` - Criar router para produtos separado do main
- `exercicio_2.py` - Criar sub-rota: /clientes/{id}/pedidos
- `exercicio_3.py` - Organizar o projeto do Aqualog com routers
