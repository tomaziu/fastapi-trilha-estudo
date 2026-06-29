# 08 - Middlewares e CORS

## O que é Middleware

Código que roda **antes** e **depois** de cada requisição. Útil para logs, autenticação, headers.

## CORS (Cross-Origin Resource Sharing)

Controle quais domínios podem acessar sua API. Essencial quando o frontend está em outro domínio.

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Middleware customizado

```python
import time
from starlette.middleware.base import BaseHTTPMiddleware

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start
        print(f"{request.url.path} - {duration:.2f}s")
        return response

app.add_middleware(TimerMiddleware)
```

## Exercícios

- `exercicio_1.py` - Configurar CORS para permitir localhost:3000
- `exercicio_2.py` - Criar middleware de log de requisições
- `exercicio_3.py` - Criar middleware de autenticação global
