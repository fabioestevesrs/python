from fastapi import APIRouter
from config.database import conexao
from models.jogador import Jogador
from schemas.jogador import jogador_entidade, listar_jogadores_entidades
from bson import ObjectId

jogador_router = APIRouter()


@jogador_router.get("/")
async def inicio():
    return "Bem vindo ao FullStack FARM"


@jogador_router.get("/jogadores")
async def listar_jogadores():
    return listar_jogadores_entidades(conexao.local.jogador.find())


@jogador_router.get("/jogadores/{jogador_id}")
async def buscar_jogador_id(jogador_id):
    return jogador_entidade(conexao.local.jogador.find_one({"_id": ObjectId(jogador_id)}))


@jogador_router.post("/jogadores")
async def cadastrar_jogadores(jogador: Jogador):
    conexao.local.jogador.insert_one(dict(jogador))
    return listar_jogadores_entidades(conexao.local.jogador.find())


@jogador_router.put("/jogadores/{jogador_id}")
async def atualizar_jogador(jogador_id, jogador: Jogador):
    conexao.local.jogador.find_one_and_update(
        {"_id": ObjectId(jogador_id)},
        {"$set": dict(jogador)}
    )
    return jogador_entidade(conexao.local.jogador.find_one({"_id": ObjectId(jogador_id)}))


@jogador_router.delete("/jogadores/{jogador_id}")
async def excluir_jogador(jogador_id):
    return jogador_entidade(conexao.local.jogador.find_one_and_delete({"_id": ObjectId(jogador_id)}))
