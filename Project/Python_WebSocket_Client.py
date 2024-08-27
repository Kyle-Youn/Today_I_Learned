import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Hello, WebSocket!"
        await websocket.send(message)
        print(f"Sent message: {message}")

        response = await websocket.recv()
        print(f"Received response: {response}")

asyncio.get_event_loop().run_until_complete(hello())
