# 07 - Autenticação JWT

## O que é

JWT (JSON Web Token) é um padrão para autenticação stateless. O cliente envia o token no header `Authorization: Bearer <token>`.

## Fluxo

1. Usuário faz login com email/senha
2. Backend gera token JWT
3. Cliente envia token em todas as rotas protegidas
4. Backend valida o token

## Exemplo básico

```python
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "sua-chave-secreta"
ALGORITHM = "HS256"

def criar_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
```

## Dependência para proteger rotas

```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verificar_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Token inválido")
    return user

@app.get("/pedidos")
def listar_pedidos(user=Depends(get_current_user)):
    return []
```

## Exercícios

- `exercicio_1.py` - Criar rota de login que retorna token
- `exercicio_2.py` - Proteger uma rota com dependência de auth
- `exercicio_3.py` - Extrair dados do usuário do token
