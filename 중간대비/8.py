import socket

# 외부 서버의 IP 주소와 포트 번호
SERVER_ADDR = 'www.daum.net'
SERVER_PORT = 80

# 릴레이 서버의 IP 주소와 포트 번호
RELAY_ADDR = '127.0.0.1'
RELAY_PORT = 9000

def main():
    # 릴레이 서버의 소켓 생성 및 바인드
    relay_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    relay_socket.bind((RELAY_ADDR, RELAY_PORT))
    relay_socket.listen(1)

    print('릴레이 서버가 시작되었습니다.')

    while True:
        # 브라우저의 요청 수신
        client_socket, client_addr = relay_socket.accept()
        print(f'{client_addr}에서 요청이 들어왔습니다.')

        # 외부 서버에 요청 전송
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((SERVER_ADDR, SERVER_PORT))

        # HTTP 요청 메시지 생성 및 전송
        request_line = b'GET / HTTP/1.1\r\n'
        host_header = f'Host: {SERVER_ADDR}\r\n'.encode('utf-8')
        server_socket.send(request_line)
        server_socket.send(host_header)
        server_socket.send(b'\r\n')

        # 외부 서버에서 응답 수신
        response_data = server_socket.recv(4096)
        while response_data:
            # 브라우저로 응답 전송
            client_socket.send(response_data)
            response_data = server_socket.recv(4096)

        # 소켓 종료
        server_socket.close()
        client_socket.close()

if __name__ == '__main__':
    main()