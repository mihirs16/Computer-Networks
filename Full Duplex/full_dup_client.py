import socket
import threading

host = socket.gethostname()
port = 6666
buff = 1024

client_sock = socket.socket()
client_sock.connect((host, port))

def recieve():
    while True:
        rMsg = client_sock.recv(buff).decode()
        if not rMsg:
            print('Ending connection')
            break
        print()
        print("revd:", rMsg)

def send():
    while True:
        sMsg = input()
        client_sock.send(sMsg.encode())

t1 = threading.Thread(target=send, name=1)
t2 = threading.Thread(target=recieve, name=2)

t1.start()
t2.start()