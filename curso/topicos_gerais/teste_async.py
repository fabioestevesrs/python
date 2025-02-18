import asyncio


async def tarefa1():
    print('Iniciando tarefa 1...')
    await asyncio.sleep(3)
    print('Finalizando tarefa 1...')


async def tarefa2():
    print('Iniciando tarefa 2...')
    await asyncio.sleep(2)
    print('Finalizando tarefa 2...')


async def tarefa3():
    print('Iniciando tarefa 3...')
    await asyncio.sleep(5)
    print('Finalizando tarefa 3...')


async def main():
    await asyncio.gather(
        tarefa1(),
        tarefa2(),
        tarefa3()
    )


asyncio.run(main())
