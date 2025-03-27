from pydantic import BaseModel


class Jogador(BaseModel):
    nome: str
    idade: int
    time: str
