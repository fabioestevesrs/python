def encontre_indices(lista, item):
    lista_indices = []

    for indice, valor in enumerate(lista):
        if valor == item:
            lista_indices.append([indice])
        elif isinstance(lista[indice], list):
            for i in encontre_indices(lista[indice], item):
                lista_indices.append([indice] + i)

    return lista_indices


if __name__ == '__main__':
    print(encontre_indices([[[1, 2, 3], 2, [1, 3], [1, 2, 3]], [1, 2, 3]], 2))
