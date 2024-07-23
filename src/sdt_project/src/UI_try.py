import asyncio
import websockets

async def send_data(uri, data):
    async with websockets.connect(uri) as websocket:
        # Veriyi WebSocket üzerinden gönder
        await websocket.send(data)
        print(f"Sent: {data}")

# WebSocket sunucusunun URI'si
uri = "ws://10.7.91.190:5216/"

# Gönderilecek veri
data = "Hello, WebSocket!"

# Veri gönderimini başlat
asyncio.get_event_loop().run_until_complete(send_data(uri, data))
