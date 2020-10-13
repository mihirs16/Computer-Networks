import socket
host = socket.gethostname()
port = 6666
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
print("Wait State...")
while True:
  sentence, addr = s.recvfrom(1024)
  print('Client: ', sentence.decode())
  if(sentence == '/EXIT/'):
    break
  message = sentence.decode()
  s.sendto(message.encode(), addr)
  message = input(">> ")
  s.sendto(message.encode(), addr)
s.close()