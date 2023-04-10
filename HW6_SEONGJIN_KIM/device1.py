import socket
import random
import time

# 디바이스1 TCP 서버 설정
host = '127.0.0.1'
port = 9000

# TCP 서버 열기
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)
print(f"Device 1 TCP server is listening on {host}:{port}")

while True:
    # 클라이언트 연결 대기
    conn, addr = sock.accept()
    print(f"Connected by {addr}")

    # 클라이언트로부터 메시지 수신 및 처리
    while True:
        data = conn.recv(1024).decode()
        if data == "Request":
            # 온도, 습도, 조도 랜덤으로 생성
            temp = random.randint(0, 40)
            humid = random.randint(0, 100)
            illum = random.randint(70, 150)
            # 생성한 값 클라이언트에 전송
            conn.sendall(f"Temp={temp}, Humid={humid}, Illum={illum}".encode())
            conn.close()
            break
        elif data == "quit":
            # 종료 메시지 수신 시 TCP 서버 종료
            conn.sendall("quit".encode())
            conn.close()
            sock.close()
            break