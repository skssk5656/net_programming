import socket
import select
import random

def handle_request(client_socket):
    request = client_socket.recv(1024).decode()
    if request == '1':
        temperature = random.randint(0, 40)
        response = f"Temp={temperature}"
    elif request == '2':
        humidity = random.randint(0, 100)
        response = f"Humid={humidity}"
    else:
        response = "Invalid request"

    client_socket.send(response.encode())

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9999)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print('서버 시작 - localhost:9999')

    sockets = [server_socket]

    while True:
        readable, _, _ = select.select(sockets, [], [])

        for sock in readable:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                sockets.append(client_socket)
                print('클라이언트 접속:', client_address)
            else:
                try:
                    handle_request(sock)
                except ConnectionResetError:
                    print('클라이언트 접속 종료:', sock.getpeername())
                    sock.close()
                    sockets.remove(sock)

    server_socket.close()

run_server()
