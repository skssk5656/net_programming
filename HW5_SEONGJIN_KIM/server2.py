import socket
import os

def main():
    # create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind socket to a public host, and a port
    server_socket.bind(('localhost', 80))

    # become a server socket
    server_socket.listen(5)

    print('Server is listening...')

    while True:
        # accept connections from outside
        (client_socket, client_address) = server_socket.accept()

        # read first line of HTTP request
        request = client_socket.recv(1024).decode()

        # parse filename from request
        filename = request.split()[1][1:]

        # set mimeType
        if filename.endswith('.html'):
            mimeType = 'text/html; charset=utf-8'
        elif filename.endswith('.png'):
            mimeType = 'image/png'
        elif filename.endswith('.ico'):
            mimeType = 'image/x-icon'
        else:
            # if file not found, send 404 response
            if not os.path.exists(filename):
                response_headers =  'HTTP/1.1 404 Not Found\r\n\r\n'
                response_content = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
                client_socket.send(response_headers.encode() + response_content.encode())
                client_socket.close()
                continue

            continue

        try:
            # open the file and read its content
            with open(filename, 'rb') as file:
                content = file.read()

            # send HTTP response headers
            response_headers = 'HTTP/1.1 200 OK\nContent-Type: {}\nContent-Length: {}\n\n'.format(mimeType, len(content))
            client_socket.send(response_headers.encode())

            # send HTTP response content
            if mimeType == 'text/html':
                client_socket.send(content.decode('utf-8').encode())
            else:
                client_socket.send(content)

            client_socket.close()
        except IOError:
            # file not found
            response_headers = 'HTTP/1.1 404 Not Found\r\n\r\n'
            response_content = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
            client_socket.send(response_headers.encode() + response_content.encode())

if __name__ == '__main__':
    main()
