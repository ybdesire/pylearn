#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print("recv: {0}".format(name))

    greeting = "Hello {0}!".format(name)

    await websocket.send(greeting)
    print("send: {0}".format(greeting))

start_server = websockets.serve(hello, 'localhost', 8765)# port 8765

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
