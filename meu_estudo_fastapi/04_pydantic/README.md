# 04 - Pydantic e Validação de Dados

## O que é

Pydantic valida e organiza dados automaticamente. FastAPI usa para:
- Validar entrada (body, query)
- Definir schemas de saída
- Gerar documentação

## Modelo básico

```python
from pydantic import BaseModel
from typing import Optional

class ClienteCreate(BaseModel):
    nome: str
    telefone: str
    endereco: Optional[str] = None

class ClienteResponse(BaseModel):
    id: int
    nome: str
    telefone: str
```

## Validações úteis

```python
from pydantic import Field

class Pedido(BaseModel):
    quantidade: int = Field(gt=0, description="Deve ser maior que 0")
    status: str = Field(default="pendente", pattern="^(pendente|entregue|cancelado)$")
```

## Exercícios

- `exercicio_1.py` - Criar schema para Produto com validação de preço > 0
- `exercicio_2.py` - Criar schema de resposta com campos ocultos
- `exercicio_3.py` - Usar Field para validações customizadas
