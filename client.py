# import asyncio
# import websockets

# async def hello():
#     uri = "ws://localhost:8765"
#     async with websockets.connect(uri) as websocket:
#         name = input("What is your name?")

#         await websocket.send(name)
#         print(f"Client Sent: {name}")

#         greeting = await websocket.recv()
#         print(f"client recevied : {greeting}")

# if __name__ == "__main__":
#     asyncio.run(hello())

import asyncio
import websockets

# This async function handles the WebSocket client connection
async def hello():
    uri = "ws://localhost:8765"  # WebSocket server address
    async with websockets.connect(uri) as websocket:
        # Ask the user for input
        name = input("What is your name? ")

        # Send the name to the server
        await websocket.send(name)
        print(f"Client Sent: {name}")

        # Wait for the greeting from the server
        greeting = await websocket.recv()
        print(f"Client Received: {greeting}")

# Run the async client
if __name__ == "__main__":
    asyncio.run(hello())
