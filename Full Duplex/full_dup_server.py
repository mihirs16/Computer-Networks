import socket
import threading

host = socket.gethostname()
port = 6666
buff = 1024
s = socket.socket(socket.SOCK_DGRAM)
s.bind((host, port))
s.listen(5)

print('waiting for a conn...')
client_sock, cADDR = s.accept()

def recieve():
    while True:
        rMsg = client_sock.recv(buff).decode()
        if not rMsg:
            print('Ending connection')
            break
        print()
        print("recvd: " + rMsg)

def send():
    while True:
        sMsg = input()
        if not sMsg:
            break
        client_sock.send(sMsg.encode())

t1 = threading.Thread(target=send, name=3)
t2 = threading.Thread(target=recieve, name=4)

t1.start()
t2.start()

