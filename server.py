import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Your message to me was\n>>> {message}")
        if "javascript" in message:
            message = message.replace("javascript", "python")
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", 7560):
        await asyncio.Future() # Run forever

if __name__ == "__main__":
    asyncio.run(main())
