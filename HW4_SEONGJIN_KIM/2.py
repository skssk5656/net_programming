import socket

def calculate(expression):
    # 입력받은 계산식을 파싱하여 연산 수행
    operator = ""
    if "+" in expression:
        operator = "+"
    elif "-" in expression:
        operator = "-"
    elif "*" in expression:
        operator = "*"
    elif "/" in expression:
        operator = "/"
    
    operands = expression.split(operator)
    operand1 = int(operands[0].strip())
    operand2 = int(operands[1].strip())
    
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = round(operand1 / operand2, 1)
        
    return result

HOST = '127.0.0.1'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, 9000))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            expression = data.decode("utf-8")
            if expression == "q":
                break
            result = calculate(expression)
            conn.sendall(str(result).encode("utf-8"))