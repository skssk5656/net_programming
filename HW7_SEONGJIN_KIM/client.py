import socket
import threading


def handler(sock, my_addr):
    while True:
        msg = sock.recv(1024).decode()
        if not msg:
            break
        if my_addr != msg.split()[0][1:-1]:
            print(msg)


svr_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(svr_addr)

my_id = input('ID를 입력하세요: ')
sock.send(('['+my_id+']').encode())

th = threading.Thread(target=handler, args=(sock, my_id))
th.daemon = True
th.start()

while True:
    msg = input()
    sock.send(('[' + my_id + '] ' + msg).encode())
