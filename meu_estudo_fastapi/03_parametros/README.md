# 03 - Parâmetros (Path, Query, Body)

## Tipos de parâmetro

### Path Parameter
Valor na URL: `/clientes/{cliente_id}`

```python
@app.get("/clientes/{cliente_id}")
def buscar_cliente(cliente_id: int):
    return {"cliente_id": cliente_id}
```

### Query Parameter
Parâmetro na query string: `/pedidos?status=pendente`

```python
@app.get("/pedidos")
def listar_pedidos(status: str = None):
    return {"status": status}
```

### Body Parameter
Dados no corpo da requisição (JSON):

```python
from pydantic import BaseModel

class Cliente(BaseModel):
    nome: str
    telefone: str

@app.post("/clientes")
def criar_cliente(cliente: Cliente):
    return cliente
```

## Exercícios

- `exercicio_1.py` - Criar rota com path parameter para buscar produto por ID
- `exercicio_2.py` - Criar rota com query parameter para filtrar pedidos por status
- `exercicio_3.py` - Criar rota POST com body parameter para criar cliente
