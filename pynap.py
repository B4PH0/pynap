from utils.painel import painel
from utils.args import parse
import asyncio
import warnings

warnings.filterwarnings("ignore")
async def check_port(host, port):
    try:
        reader, writer = await asyncio.open_connection(host, port)
        writer.close()
        await writer.wait_closed()
        return True
    except (ConnectionRefusedError, asyncio.TimeoutError):
        pass

async def main():
    painel()
    host = parse()
    ports = [80, 443, 22, 25, 53, 21, 110, 111, 143, 3389, 3306, 23, 8080, 137, 161, 389, 465, 587, 636, 993, 995, 1433, 1521, 5432, 9929, 31337]
    portas = sorted(ports)
    for index, port in enumerate(portas):
        if await check_port(host, port):
            print(f'{port} open')

asyncio.run(main())