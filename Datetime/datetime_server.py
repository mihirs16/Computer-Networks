import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2467
s.bind((host, port))
s.listen(14)
print("Waiting...")
while True:
    conn, addr = s.accept()
    print("Connected Successfully")
    date = time.strftime("%c")
    message = str(date)
    conn.send(message.encode())
    conn.close()