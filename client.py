import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6986
s.connect((host,port))
inp = input("Input: ")
s.send(bytes(inp,'utf-8'))
while True:
    data = s.recv(1024)
    if data == 'quit' or not data:
        print("Quiting")
        break
    else:
        print("Server:",data.decode())
        msg = input("Client: ")
        s.send(msg.encode())
s.close()