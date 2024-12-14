import re
from unidecode import unidecode


def palindromo(texto: str) -> bool:
    texto_sem_acentuacao = unidecode(texto)
    texto_somente_letras = re.sub(r'[^a-zA-Z]', '', texto_sem_acentuacao).lower()
    texto_invertido = texto_somente_letras[::-1]

    return texto_somente_letras == texto_invertido


if __name__ == '__main__':
    print(palindromo('Olá Mundo!'))
    print(palindromo('arara'))
    print(palindromo('Socorram-me! Subi no ônibus em Marrocos!'))
