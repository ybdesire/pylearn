#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def hello():
    async with websockets.connect(
            'ws://localhost:8765') as websocket:
        name = "Test"

        await websocket.send(name)
        print("send: {0}".format(name))

        greeting = await websocket.recv()
        print("rcv: {0}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())
