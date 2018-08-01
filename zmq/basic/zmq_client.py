import zmq

# client
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://127.0.0.1:5555')
socket.send('test')
msg = socket.recv()
print msg
