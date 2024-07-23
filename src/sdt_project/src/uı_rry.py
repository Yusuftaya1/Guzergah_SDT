#!/usr/bin/env python

from websockets.sync.client import connect

def hello():
    with connect("ws://10.7.91.190:5216/myhub") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

hello()