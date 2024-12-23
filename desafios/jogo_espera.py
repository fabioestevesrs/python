import time
import random

def jogo_espera():
    objetivo = random.randint(2, 4)
    print(f'Objetivo em segundos: {objetivo}')

    input('-- Pressione Enter para começar --')
    inicio = time.perf_counter()

    input(f'-- Pressione Enter novamente depois de {objetivo} segundos --')
    tempo_total = time.perf_counter() - inicio

    if (tempo_total == objetivo):
        print('Perfeito!')
    elif tempo_total < objetivo:
        print(f'Rápido demais ({tempo_total} segundos)')
    else:
        print(f'Muito lento! ({tempo_total} segundos)')

if __name__ == '__main__':
    jogo_espera()