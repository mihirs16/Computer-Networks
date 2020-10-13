import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2467
client.connect((host, port))
message = client.recv(1024)
print ("Time:", message.decode())
client.close()