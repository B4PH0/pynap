import socket
import asyncio
from args import *

def scan():
    async def testar_porta(host, porta):
        try:
            reader, writer = await asyncio.open_connection(host, porta)
            return print(f'{porta} OPEN')
            writer.close()
            await writer.wait_closed()
        except (ConnectionRefusedError, socket.gaierror):
            pass

    async def varrer_portas(host, porta_inicial, porta_final):
        tasks = []
        for porta in range(porta_inicial, porta_final):
            tasks.append(asyncio.create_task(testar_porta(host, porta)))
        await asyncio.wait(tasks)

    if __name__ == '__main__':
        arg = parse()
        porta_inicial = 1
        porta_final = 100
        asyncio.run(varrer_portas(arg, porta_inicial, porta_final))

scan()