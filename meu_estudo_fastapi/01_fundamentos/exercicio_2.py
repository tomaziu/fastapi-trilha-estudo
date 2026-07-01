from fastapi import FastAPI

app = FastAPI()

@app.get("/usuarios")
def minha_rota():
    return {
        "usuario1": "Thomaz",
        "usuario2": "Joana",
        "usuario3": "Cebolão"
    }

@app.post("/rota")
def minha_rota_post(dados: str):
    return {"mensagem": f"Recebi: {dados}"}