from http.server import BaseHTTPRequestHandler, HTTPServer

# 서버의 요청을 처리하는 핸들러 클래스 정의
class ImageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            
            # iot.png 파일을 읽어서 전송
            with open('iot.png', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')

# 서버 설정 및 실행
def run():
    server_address = ('localhost', 8888)
    httpd = HTTPServer(server_address, ImageHandler)
    print('서버 시작 - http://localhost:8888/')
    httpd.serve_forever()

run()