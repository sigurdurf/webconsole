import asyncio
import websockets
from test_program import Calculator

async def echo(websocket, path):
    calc = Calculator()
    async for message in websocket:
        await websocket.send("Your message to me was:\r\n")
        await websocket.send(f">>> {message}\r\n")
        if "javascript" in message:
            message = message.replace("javascript", "python")
        equation = calc.format_equation(message)
        result = calc.calculate(equation)

        await websocket.send("My response to that is:\r\n")
        await websocket.send(f">>> {result}\r\n")

async def main():
    async with websockets.serve(echo, "localhost", 7560):
        await asyncio.Future() # Run forever

if __name__ == "__main__":
    asyncio.run(main())
