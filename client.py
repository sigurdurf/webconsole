import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:7560") as websocket:
        await websocket.send("Hello")
        response = await websocket.recv()
        print(f">>> {response}")


asyncio.run(hello())
