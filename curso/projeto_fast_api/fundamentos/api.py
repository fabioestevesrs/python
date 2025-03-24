from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

jogadores = {
    1: {
        "nome": "Coutinho",
        "idade": 34,
        "time": "Vasco"
    },
    2: {
        "nome": "Gustavo",
        "idade": 29,
        "time": "Palmeiras"
    }
}


class Jogador(BaseModel):
    nome: str
    idade: int
    time: str


class AtualizaJogador(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    time: Optional[str] = None


# get-jogador/1 - Path parameter

# get-jogador/?id=1 - Query parameter
# get-jogador-time/?time="asd"

@app.get("/get_jogador/{id_jogador}")
def get_jogador(id_jogador: int):
    return jogadores[id_jogador]


@app.get("/get_jogador_time")
def get_jogador_time(time: str):
    print(jogadores)
    for jogador_id in jogadores:
        if jogadores[jogador_id]["time"] == time:
            return jogadores[jogador_id]
    return {"Dados": "Time não encontrado."}


@app.get("/")
def inicio():
    return jogadores


@app.post("/cadastrar-jogador/{jogador_id}")
def cadastrar_jogador(jogador_id: int, jogador: Jogador):
    if jogador_id in jogadores:
        return {"Erro": "Jogador já existe."}

    jogadores[jogador_id] = jogador
    return jogadores[jogador_id]


@app.put("/atualizar-jogador/{jogador_id}")
def atualizar_jogador(jogador_id: int, jogador: AtualizaJogador):
    if (jogador_id not in jogadores):
        return {"Erro": "Jogador não encontrado."}

    if jogador.nome != None:
        jogadores[jogador_id]["nome"] = jogador.nome

    if jogador.idade != None:
        jogadores[jogador_id]["idade"] = jogador.idade

    if jogador.time != None:
        jogadores[jogador_id]["time"] = jogador.time

    return jogadores[jogador_id]


@app.delete("/excluir-jogador/{jogador_id}")
def excluir_jogador(jogador_id: int):
    if (jogador_id not in jogadores):
        return {"Erro": "Jogador não encontrado."}
    del jogadores[jogador_id]

    return {"Mensagem": "Jogador excluído com sucesso."}
