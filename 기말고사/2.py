import socket
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    if request.startswith("GET / HTTP/1.1"):
        status_line = "HTTP/1.1 200 OK\r\n"
        content_type = "Content-Type: image/png\r\n"
        end_of_headers = "\r\n"
        response = status_line + content_type + end_of_headers

        with open("iot.png", "rb") as file:
            response_bytes = response.encode()
            response_bytes += file.read()

        client_socket.sendall(response_bytes)

    client_socket.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 8888)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print("서버 시작 - http://localhost:8888/")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

run_server()
