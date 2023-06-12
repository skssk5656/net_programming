import selectors
import socket
import random

def handle_request(sock):
    request = sock.recv(1024).decode()
    if request == '1':
        temperature = random.randint(0, 40)
        response = f"Temp={temperature}"
    elif request == '2':
        humidity = random.randint(0, 100)
        response = f"Humid={humidity}"
    else:
        response = "Invalid request"

    sock.send(response.encode())

def accept_connection(sock):
    client_socket, client_address = sock.accept()
    print('클라이언트 접속:', client_address)
    client_socket.setblocking(False)
    events = selectors.EVENT_READ
    data = {'socket': client_socket, 'addr': client_address}
    selector.register(client_socket, events, data=data)

def close_connection(sock):
    data = sock.data
    print('클라이언트 접속 종료:', data['addr'])
    selector.unregister(sock)
    sock.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9999)
    server_socket.bind(server_address)
    server_socket.listen(5)
    server_socket.setblocking(False)
    print('서버 시작 - localhost:9999')

    global selector
    selector = selectors.DefaultSelector()
    events = selectors.EVENT_READ
    data = {'socket': server_socket}
    selector.register(server_socket, events, data=data)

    while True:
        events = selector.select()

        for key, _ in events:
            sock = key.fileobj

            if sock == server_socket:
                accept_connection(sock)
            else:
                try:
                    handle_request(sock)
                except ConnectionResetError:
                    close_connection(sock)

run_server()
