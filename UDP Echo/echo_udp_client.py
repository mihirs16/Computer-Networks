import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 1234
host = socket.gethostname()

while True:
	msg = input('Message to be echoed: ').encode('utf_8')
	sent = sock.sendto(msg, (host, port))
	if msg.decode() == 'EXIT':
		break
	data, address = sock.recvfrom(4096)
	print("received echoed data:",data.decode())