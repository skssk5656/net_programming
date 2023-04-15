import socket
import time  # 시간 모듈을 import

port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('Enter a message: ')
    if msg == 'q':
        break

    num_retries = 0
    while num_retries < 4:  # 최대 3회의 재전송 (최초 메시지 포함 최대 4번 전송)
        sock.sendto(msg.encode(), ('localhost', port))
        sock.settimeout(1)  # 1초 동안 서버로부터 응답을 기다림

        try:
            data, addr = sock.recvfrom(BUFFSIZE)
            print('Server says: ', data.decode())
            break  # 정상적인 응답을 받으면 반복문 종료
        except socket.timeout:  # 응답이 없는 경우
            num_retries += 1
            print('Retry', num_retries)  # 재전송 횟수 출력
            continue  # 재전송

    if num_retries == 4:  # 최대 재전송 횟수를 초과한 경우
        print('Server does not respond. Exiting...')
        break

sock.close()