from fastapi import FastAPI

app = FastAPI()

produtos = [{
      "id": 1,
      "nome": "caderno",
      "preco": 10
    }]

@app.get("/produtos")
def listar_produtos():
    return {"produtos": produtos}
    
@app.post("/produtos")
def adicionar_produtos(nome:str, preco:int):
    produto = {"id": len(produtos) + 1, "nome": nome, "preco": preco}
    produtos.append(produto)
    return {"mensagem": f"Produto adicionado com sucesso!"}

@app.put("/produtos/{produto_id}")
def atualizar_produtos(produto_id: int, nome: str, preco: int):
    if produto_id < 1 or produto_id > len(produtos):
        return {"mensagem": "ID inválido!"}
    for p in produtos:
        if p["id"] == produto_id:
            p["nome"] = nome
            p["preco"] = preco
            return {"mensagem": "Produto atualizado com sucesso!"}

@app.delete("/produtos/{produto_id}")
def deletar_produtos(produto_id: int):
    if produto_id < 1 or produto_id > len(produtos):
        return {"mensagem": "ID inválido!"}
    for i, p in enumerate(produtos):
        if p["id"] == produto_id:
            produtos.pop(i)
            return {"mensagem": f"Produto {produto_id} removido"}