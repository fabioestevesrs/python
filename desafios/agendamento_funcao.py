import sched
import time

s = sched.scheduler(time.time, time.sleep)


def agendamento(horario_evento, funcao, prioridade, *args):
    s.enterabs(horario_evento, prioridade, funcao, argument=args)
    t = time.asctime(time.localtime(horario_evento))
    print(f'{funcao.__name__}() agendado para {t} - Prioridade: {prioridade}')


if __name__ == '__main__':
    prioridade = 1
    agendamento(time.time() + 3, print, prioridade, 'Executando 1...')
    prioridade += 1
    agendamento(time.time() + 6, print, prioridade, 'Executando 2...')
    prioridade += 1
    agendamento(time.time() + 9, print, prioridade, 'Executando 3...')
    prioridade += 1

    print('Eventos pendentes:')

    for evento in s.queue:
        print(evento)

    s.run()
