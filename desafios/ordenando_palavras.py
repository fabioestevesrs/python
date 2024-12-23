def ordenar_palavras(frase: str) -> str:
    return " ".join(sorted(frase.split(), key=lambda palavra: palavra.lower()))


if __name__ == '__main__':
    print(ordenar_palavras("Olá mundo!"))
    print(ordenar_palavras("maçã LARANJA banana"))
