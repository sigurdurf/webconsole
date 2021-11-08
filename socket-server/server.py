import os
import asyncio
import websockets
from test_program import Calculator


async def on_message(websocket, path):
    calc = Calculator()
    await websocket.send("Enter an eqation: ")
    async for message in websocket:
        await websocket.send("Your message to me was:\r\n")
        await websocket.send(f">>> {message}\r\n")
        if "javascript" in message:
            message = message.replace("javascript", "python")
        equation = calc.format_equation(message)
        result = calc.calculate(equation)

        await websocket.send("My response to that is:\r\n")
        await websocket.send(f">>> {result}\r\n")
        await websocket.send("Enter an equation: ")

async def main():
    port = int(os.environ.get('PORT', 7560))
    async with websockets.serve(on_message, "0.0.0.0", port):
        print(f"Running on port: {port}")
        await asyncio.Future() # Run forever

if __name__ == "__main__":
    asyncio.run(main())
