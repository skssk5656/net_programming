import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 5004

# 서버에 연결
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

while True:
    # 사용자로부터 명령어 입력 받기
    data = input("명령어 입력 (send [mboxID] message / receive [mboxID] / quit): ").strip()
    sock.send(data.encode())

    # 서버로부터 응답 받기
    response = sock.recv(1024).decode()
    print( response)

    # quit 명령어를 입력한 경우 클라이언트 종료
    if data == "quit":
        print("클라이언트를 종료합니다.")
        sock.close()
        break