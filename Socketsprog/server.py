import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3434))
s.listen(5)   # listen with a queue of 5

while True:
    clinetSocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clinetSocket.send(bytes("Hello, welcome to the server!", "utf-8"))