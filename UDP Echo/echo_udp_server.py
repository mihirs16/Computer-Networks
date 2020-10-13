import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 1234
host = socket.gethostname()

sock.bind((host, port))
print('Waiting for response')

while True:
	data, add  = sock.recvfrom(4096)
	print("received data, echo back")
	if data:
		if data.decode() == 'EXIT':
			break
		else:
			sent = sock.sendto(data, add)