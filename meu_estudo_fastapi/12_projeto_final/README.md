# 12 - Projeto Final: API de Gestão de Pedidos

## Objetivo

Criar uma API REST completa aplicando **todos** os tópicos da trilha.

## Funcionalidades

1. Cadastrar cliente (nome, telefone, endereço)
2. Criar pedido (cliente_id, quantidade, status)
3. Listar pedidos com filtro por status
4. Atualizar status do pedido (pendente → entregue)
5. Autenticação JWT (apenas usuários logados podem criar/atualizar)
6. Retornar erros claros com HTTPException

## Estrutura

```
12_projeto_final/
├── main.py
├── database.py
├── models/
│   ├── models.py
│   └── schemas.py
├── routers/
│   ├── auth.py
│   ├── clientes.py
│   └── pedidos.py
├── tests/
│   ├── test_auth.py
│   ├── test_clientes.py
│   └── test_pedidos.py
└── requirements.txt
```

## Checklist

- [ ] Pydantic para validação de entrada e saída
- [ ] SQLAlchemy com sessão via Depends
- [ ] Autenticação JWT com token Bearer
- [ ] Testes com pytest cobrindo pelo menos 3 rotas
- [ ] Organização com routers separados
- [ ] Tratamento de erros com HTTPException
- [ ] CORS configurado
- [ ] README com instruções de uso

## Exercícios

- `exercicio_1.py` - Estrutura base do projeto
- `exercicio_2.py` - CRUD de clientes completo
- `exercicio_3.py` - CRUD de pedidos com filtro
- `exercicio_4.py` - Autenticação JWT
- `exercicio_5.py` - Testes com pytest
