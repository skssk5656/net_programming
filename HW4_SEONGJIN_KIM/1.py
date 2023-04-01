import socket

HOST = '127.0.0.1'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, 9000))
    while True:
        expression = input("계산식을 입력하세요(피연산자: 정수, 지원연산: +, -, *, /): ")
        if expression == "q":
            s.sendall(expression.encode("utf-8"))
            break
        s.sendall(expression.encode("utf-8"))
        data = s.recv(1024)
        result = data.decode("utf-8")
        print("결과: ", result)