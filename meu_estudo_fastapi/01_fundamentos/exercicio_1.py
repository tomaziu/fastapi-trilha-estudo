from fastapi import FastAPI

app = FastAPI()

@app.get("/nome")
def meu_nome():
    return {"nome": "Thomaz"}
