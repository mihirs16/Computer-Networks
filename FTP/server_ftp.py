import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5120
s.bind((host,port))
print("Waiting for connection...")
s.listen(5)
conn, addr = s.accept()
print('received from:', addr[0])
while True:
    x = conn.recv(1024).decode()
    f = open(x, 'r')
    y = f.read()
    conn.send(y.encode())
    f.close()
    break
conn.close()
