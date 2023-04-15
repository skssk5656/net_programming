import socket

# 호스트와 포트 설정
HOST = "127.0.0.1"  # 호스트 주소
PORT = 5004       # 포트 번호

# 메일 박스를 저장할 딕셔너리
mailboxes = {}

# TCP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 소켓 바인딩
sock.bind((HOST, PORT))
# 소켓 리스닝
sock.listen(5)
print(f"서버가 {HOST}:{PORT}에서 시작되었습니다.")

while True:
    # 클라이언트로부터 연결 요청 수락
    conn, addr = sock.accept()
    print(f"클라이언트로부터 연결 수락: {addr}")
    # 연결된 클라이언트와 통신
    while True:
        data = conn.recv(1024).decode()
        if not data:
            # 클라이언트로부터 데이터를 받지 못한 경우 연결 종료
            print("클라이언트 연결이 종료되었습니다.")
            break
        # 수신한 메시지를 공백을 기준으로 분리하여 명령어와 인자로 분리
        tokens = data.split()
        command = tokens[0]

        if command == "send":
            # "send" 명령어 처리
            mbox_id = tokens[1]
            message = " ".join(tokens[2:])
            if mbox_id in mailboxes:
                # 메일 박스가 이미 존재하는 경우 메시지 저장
                mailboxes[mbox_id].append(message)
            else:
                # 메일 박스가 존재하지 않는 경우 새로 생성하고 메시지 저장
                mailboxes[mbox_id] = [message]
            # 클라이언트로 "OK" 전송
            conn.send("OK".encode())
        elif command == "receive":
            # "receive" 명령어 처리
            mbox_id = tokens[1]
            if mbox_id in mailboxes and len(mailboxes[mbox_id]) > 0:
                # 메일 박스가 존재하고 메시지가 있는 경우 제일 앞에 있는 메시지 전송 후 삭제
                message = mailboxes[mbox_id].pop(0)
                conn.send(message.encode())
            else:
                # 메일 박스가 존재하지 않거나 메시지가 없는 경우 "No messages" 전송
                conn.send("No messages".encode())
        elif command == "quit":
            # "quit" 명령어 처리
            # 클라이언트와 연결 종료
            conn.close()
            print("클라이언트 연결이 종료되었습니다.")
            break

# 서버 소켓 닫기
sock.close()