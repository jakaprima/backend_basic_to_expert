import asyncio
import websockets


async def connect():
    uri = "ws://localhost:8765"  # Replace with your server's URL
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello from the client!")
        response = await websocket.recv()
        print(f"Received from server: {response}")

asyncio.run(connect())
