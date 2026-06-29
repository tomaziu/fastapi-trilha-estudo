# 11 - Boas Práticas (Depends, Lifespan, Async)

## Depends (Injeção de Dependência)

Usar `Depends` para compartilhar lógica (sessão DB, auth, etc.):

```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/clientes")
def listar(db: Session = Depends(get_db)):
    return db.query(Cliente).all()
```

## Lifespan (init/shutdown)

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Iniciando API...")
    yield
    # Shutdown
    print("Encerrando API...")

app = FastAPI(lifespan=lifespan)
```

## Async/await

FastAPI é async por padrão. Use `async def` para rotas que fazem I/O:

```python
import httpx

@app.get("/external")
async def buscar_externo():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com")
        return response.json()
```

## Dicas

- Use `async def` quando a rota faz I/O (HTTP, DB async)
- Use `def` quando a rota é computacional
- Sempre use `Depends` para sessão de banco
- Nunca crie sessão diretamente na rota

## Exercícios

- `exercicio_1.py` - Refatorar projeto para usar Depends em todas as rotas
- `exercicio_2.py` - Adicionar lifespan para inicializar banco
- `exercicio_3.py` - Criar rota async que busca dados externos
