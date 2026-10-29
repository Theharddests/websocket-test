import asyncio
import json
import os

from aiohttp import web, WSMsgType

async def home(request):
return web.json_response({
"status": "online",
"service": "WebSocket test",
"websocket_path": "/ws"
})

async def websocket_handler(request):
ws = web.WebSocketResponse()
await ws.prepare(request)

await ws.send_json({
    "status": "connected",
    "message": "WebSocket fonctionne !"
})

async for msg in ws:
    if msg.type == WSMsgType.TEXT:
        await ws.send_json({
            "echo": msg.data
        })
    elif msg.type == WSMsgType.ERROR:
        print("Erreur WebSocket :", ws.exception())

return ws

app = web.Application()
app.router.add_get("/", home)
app.router.add_get("/ws", websocket_handler)

if name == "main":
port = int(os.environ.get("PORT", "10000"))
web.run_app(app, host="0.0.0.0", port=port)