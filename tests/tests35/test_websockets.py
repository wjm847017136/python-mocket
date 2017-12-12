import asyncio
import websockets
from unittest import TestCase

from mocket.mocket import mocketize
from mocket.mockhttp import Entry


class AsyncioWebsocketsTestCase(TestCase):

    @mocketize
    def test_websockets(self):

        url = 'ws://localhost:8765'
        body = 'Hello world!'

        # Entry.single_register(
        #     Entry.GET,
        #     url,
        #     body=body,
        #     status=101,
        #     headers={
        #         'Sec-WebSocket-Accept': 'HSmrc0sMlYUkAGmm5OPpG2HaGWk=',
        #         'Upgrade': 'websocket',
        #         'Connection': 'Upgrade',
        #         'Sec - WebSocket - Accept': 'HSmrc0sMlYUkAGmm5OPpG2HaGWk =',
        #         'Sec - WebSocket - Protocol': 'chat',
        #     },
        # )

        async def hello(uri):
            async with websockets.connect(uri) as websocket:
                await websocket.send(body)

        asyncio.get_event_loop().run_until_complete(
            hello('ws://localhost:8765')
        )
