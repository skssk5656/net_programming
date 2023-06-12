import asyncio
import random

async def handle_client(reader, writer):
    try:
        request = await reader.read(1)
        if request == b'1':
            temperature = random.randint(0, 40)
            response = f'Temp={temperature}'.encode()
        elif request == b'2':
            humidity = random.randint(0, 100)
            response = f'Humid={humidity}'.encode()
        else:
            response = b'Invalid request'
        writer.write(response)
        await writer.drain()
        writer.close()
    except (ConnectionResetError, ConnectionAbortedError):
        writer.close()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 9999)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
