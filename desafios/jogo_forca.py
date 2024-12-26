import random


def escolher_tema_palavra():
    palavras_temas = {
        'cores': ['azul', 'amarelo', 'vermelho', 'verde'],
        'carros': ['cruze', 'versa', 'santana', 'onix'],
        'times': ['gremio', 'internacional', 'cruzeiro', 'flamengo'],
        'selecoes': ['brasil', 'alemanha', 'italia', 'argentina']
    }

    tema = random.choice(list(palavras_temas.keys()))
    palavra = random.choice(palavras_temas[tema])

    return tema, palavra


def mostrar_informacoes(palavra, tema, tentativas, chutes):
    print(f'Tema: {tema}\nPalavra: ', end="")
    for letra in palavra:
        print(letra if letra in chutes else "_", end="")
    print(f'\nTentativas restantes: {tentativas}')

    letras_utilizadas = ', '.join(map(str, chutes))
    print(f'Letras utilizadas: {letras_utilizadas}')


def jogo_forca():
    tema, palavra = escolher_tema_palavra()
    tentativas = len(palavra) - 1
    chutes = set()

    while tentativas > 0:
        mostrar_informacoes(palavra, tema, tentativas, chutes)
        chute = input('Escolha uma letra: ').lower()

        if chute in chutes:
            print('Letra já informada.\n')
            continue

        chutes.add(chute)

        if chute not in palavra:
            tentativas -= 1
            print('')
            continue

        if tentativas == 0:
            print(f'Perdeu! A palavra é {palavra}')
            break

        print('Acertou!\n')

        if all(letra in chutes for letra in palavra):
            print(f'Parabéns! Você acertou a palavra! ({palavra})')
            break


if __name__ == '__main__':
    jogo_forca()
