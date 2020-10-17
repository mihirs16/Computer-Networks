import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5120
s.connect((host, port))
while(True):
    y='random.txt'
    s.send(y.encode())
    x = s.recv(1024).decode()
    print(x)
    f = open('random.txt', 'w')
    f.write(x)
    f.close()
    break
s.close()
