def fatores_primos(numero: int):
    divisor = 2
    lista = []

    while divisor <= numero:
        if numero % divisor == 0:
            lista.append(divisor)
            numero = numero / divisor
        else:
            divisor += 1

    return lista


if __name__ == '__main__':
    print(fatores_primos(680))
