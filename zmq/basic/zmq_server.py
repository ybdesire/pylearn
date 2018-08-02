import zmq


# server
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://127.0.0.1:5555')
while True:
    msg = socket.recv()
    if msg == 'test':
        socket.send_string('call')
    else:
        socket.send_string('fold')
