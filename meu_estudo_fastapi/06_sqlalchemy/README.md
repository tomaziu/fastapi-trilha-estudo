# 06 - Banco de Dados com SQLAlchemy

## O que é

SQLAlchemy é o ORM (Object-Relational Mapper) mais usado com FastAPI. Mapeia tabelas do banco para classes Python.

## Configuração básica

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./banco.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
```

## Model (tabela)

```python
from sqlalchemy import Column, Integer, String
from models.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    telefone = Column(String(20))
```

## Sessão com Depends

```python
from fastapi import Depends
from sqlalchemy.orm import Session

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

## Exercícios

- `exercicio_1.py` - Criar tabela Pedido com SQLAlchemy
- `exercicio_2.py` - Fazer CRUD completo com sessão
- `exercicio_3.py` - Criar relação Cliente 1:N Pedidos
