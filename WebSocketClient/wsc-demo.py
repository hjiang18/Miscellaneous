#!/usr/bin/env python3
import json
import time
import websocket

try:
  import thread
except ImportError:
  import _thread as thread


def on_message(ws, message):
  print(message)

def on_error(ws, error):
  print(error)

def on_close(ws):
  print('### websocket closed ###')

def on_open(ws):
  def run(*args):
    for i in range(3):
      time.sleep(1)
      ts = time.strftime('%Y%m%d%H%M%S', time.localtime())
      ws.send(json.dumps({'handle':'ws-robot', 'message': 'hello %s' % ts}))
    time.sleep(1)
    ws.close()
    print('### thread terminating... ###')
  thread.start_new_thread(run, ())

if __name__ == '__main__':
# websocket.enableTrace(True)
  ws = websocket.WebSocketApp('ws://127.0.0.1:8000/chatroom/throbbing-lake-7891/',
    on_message = on_message,
    on_error = on_error,
    on_close = on_close)
  ws.on_open = on_open
  ws.run_forever()
