# 09 - Tratamento de Erros

## HTTPException

Levantar erros HTTP com mensagem clara:

```python
from fastapi import HTTPException

@app.get("/clientes/{id}")
def buscar_cliente(id: int):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not cliente:
        raise HTTPException(
            status_code=404,
            detail=f"Cliente {id} não encontrado"
        )
    return cliente
```

## Exception handlers customizados

```python
from fastapi.responses import JSONResponse

@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"erro": str(exc)}
    )
```

## Padrão de erro no Aqualog

```python
class ErrorResponse(BaseModel):
    detail: str
    status_code: int

@app.get("/pedidos/{id}", response_model=ErrorResponse)
def buscar_pedido(id: int):
    # ...
    raise HTTPException(status_code=404, detail="Pedido não encontrado")
```

## Exercícios

- `exercicio_1.py` - Criar rota que levanta 404 quando não encontra
- `exercicio_2.py` - Criar handler para erro de validação customizado
- `exercicio_3.py` - Padronizar respostas de erro com schema
