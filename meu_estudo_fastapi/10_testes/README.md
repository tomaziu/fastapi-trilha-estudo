# 10 - Testes com pytest + httpx

## Configuração

```python
# requirements.txt
pytest
httpx
```

## Teste básico

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_rota_inicial():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "API funcionando"}
```

## Testando POST

```python
def test_criar_cliente():
    response = client.post("/clientes", json={
        "nome": "João",
        "telefone": "123456789"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "João"
```

## Testando com banco de teste

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_DATABASE_URL = "sqlite:///./test.db"
test_engine = create_engine(TEST_DATABASE_URL)
TestSession = sessionmaker(bind=test_engine)

@pytest.fixture
def setup_database():
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)
```

## Exercícios

- `exercicio_1.py` - Testar rota GET inicial
- `exercicio_2.py` - Testar criação de cliente (POST)
- `exercicio_3.py` - Testar busca por ID com 404
