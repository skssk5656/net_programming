import socket

def run_client():
    server_address = ('localhost', 9999)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    print('서버에 접속 완료')

    while True:
        request = input("요청을 입력하세요 (1: 온도, 2: 습도): ")
        client_socket.send(request.encode())

        response = client_socket.recv(1024).decode()
        print("서버 응답:", response)

    client_socket.close()

run_client()