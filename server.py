import asyncio
import websockets

# This function handles communication with the client
async def hello(websocket):
    # Wait to receive a message from the client
    name = await websocket.recv()
    print(f"Server Received: {name}")

    # Prepare a greeting message
    greeting = f"Hello {name}!"

    # Send the greeting back to the client
    await websocket.send(greeting)
    print(f"Server Sent: {greeting}")

# This function sets up the server
async def main():
    # Start a WebSocket server on localhost at port 8765
    async with websockets.serve(hello, "localhost", 8765):
        # Keep the server running forever
        await asyncio.Future()

# Entry point of the script
if __name__ == "__main__":
    asyncio.run(main())
