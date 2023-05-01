import socket
import threading
import time

clients = []  # 클라이언트 목록
lock = threading.Lock()


def broadcast(msg, sender_addr):
    global clients
    with lock:
        for client in clients:
            if client[1] != sender_addr:
                client[0].send(msg)


def handle_client(sock, addr):
    global clients
    with lock:
        clients.append((sock, addr))
        print('new client', addr)
    while True:
        msg = sock.recv(1024)
        if not msg:
            continue
        if b'quit' in msg:
            print(addr, 'exited')
            with lock:
                clients.remove((sock, addr))
            sock.close()
            continue
        print(time.asctime() + str(addr) + ':' + msg.decode())
        broadcast(msg, addr)


svr_addr = ('localhost', 2500)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(svr_addr)
s.listen()

print('Server started')

while True:
    sock, addr = s.accept()
    th = threading.Thread(target=handle_client, args=(sock, addr))
    th.daemon = True
    th.start()
