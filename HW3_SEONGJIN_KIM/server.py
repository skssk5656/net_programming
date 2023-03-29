import socket
sock = socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
sock.send(b'seong jin kim')
msg1 = sock.recv(1024)
name = int.from_bytes(msg1,'big')
print(name)


sock.close()