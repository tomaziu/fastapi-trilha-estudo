# 02 - Rotas e Métodos HTTP

## O que são

Métodos HTTP definem a ação que o cliente quer executar:

| Método | Ação | Exemplo no Aqualog |
|--------|------|-------------------|
| GET | Ler dados | Listar pedidos |
| POST | Criar dados | Criar novo pedido |
| PUT | Atualizar tudo | Editar cliente completo |
| PATCH | Atualizar parcial | Mudar status do pedido |
| DELETE | Deletar dados | Remover pedido |

## Exemplo

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/clientes")
def listar_clientes():
    return [{"id": 1, "nome": "João"}]

@app.post("/clientes")
def criar_cliente():
    return {"mensagem": "Cliente criado"}

@app.put("/clientes/{cliente_id}")
def atualizar_cliente(cliente_id: int):
    return {"mensagem": f"Cliente {cliente_id} atualizado"}

@app.delete("/clientes/{cliente_id}")
def deletar_cliente(cliente_id: int):
    return {"mensagem": f"Cliente {cliente_id} removido"}
```

## Exercícios

- `exercicio_1.py` - Criar CRUD completo para "produtos"
- `exercicio_2.py` - Usar PATCH para atualização parcial
- `exercicio_3.py` - Adicionar rota para listar um único produto por ID
