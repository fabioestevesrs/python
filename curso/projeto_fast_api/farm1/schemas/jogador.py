def jogador_entidade(db_item) -> dict:
    return {
        "id": str(db_item['_id']),
        "nome": db_item['nome'],
        "idade": db_item['idade'],
        "time": db_item['time']
    }


def listar_jogadores_entidades(db_item_lista) -> list:
    lista_jogadores = []

    for item in db_item_lista:
        lista_jogadores.append(jogador_entidade(item))

    return lista_jogadores
