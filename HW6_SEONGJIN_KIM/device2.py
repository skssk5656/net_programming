import socket
import random
import time

# 디바이스 2의 IP주소와 포트번호
HOST = '127.0.0.1'
PORT = 9001

# 소켓 객체 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
print(f"Device 2 TCP server is listening on {HOST}:{PORT}")

# 클라이언트와 연결
while True:
    conn, addr = sock.accept()
    print(f"Connected by {addr}")

    while True:
        # 클라이언트가 보낸 요청 수신
        data = conn.recv(1024).decode()

        # 요청이 'Request'인 경우
        if data == 'Request':
            # 심박수, 걸음수, 소모칼로리 측정
            heartbeat = random.randint(40, 140)
            steps = random.randint(2000, 6000)
            cal = random.randint(1000, 4000)
            
            # 측정값을 문자열로 변환하여 전송
            conn.sendall(f"Heartbeat={heartbeat}, Steps={steps}, Cal={cal}".encode())
            conn.close()
            break
            # now = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
            # data = f"{now}: Device2: {message}\n"
        elif data == 'quit':
            # 클라이언트와 연결 종료
            conn.close()
            sock.close()
            break

