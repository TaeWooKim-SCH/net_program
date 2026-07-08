import asyncio
import random

PORT = 9999
BUFSIZE = 1024

async def handle_asyncclient(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    print('client :', writer.get_extra_info('peername'))
    while True:
        data = await reader.read(BUFSIZE)
        if (not data):
            writer.close()
            await writer.wait_closed()
            print('connection was closed')
            break

        decoded_data = data.decode()
        if (decoded_data == '1'):
            temperature = random.randint(0, 40) # 온도
            writer.write(f"Temp={temperature}".encode())
            await writer.drain()
        elif (decoded_data == '2'):
            humidity = random.randint(0, 100) # 습도
            writer.write(f"Humid={humidity}".encode())
            await writer.drain()

async def server_asyncmain():
    server = await asyncio.start_server(handle_asyncclient,'localhost', PORT)
    print('server started')
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(server_asyncmain())

