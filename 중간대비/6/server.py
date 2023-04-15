import socket
import random

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
   msg, addr = sock.recvfrom(BUFFSIZE)
   print('Received: ', msg.decode())

   if random.randint(1, 10) <= 4:
      continue
   
   sock.sendto(msg, addr)