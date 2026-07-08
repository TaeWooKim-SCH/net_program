from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.route()
    
    def do_POST(self):
        self.route()
    
    def route(self):
        parsed_path = parse.urlparse(self.path) # 예)self.path: /button?status=on
        real_path = parsed_path.path # 예)real.path: /button
        print(self.path, real_path)
        
        if real_path == '/':
            self.send_html('index_button.html')
        elif real_path == '/get':
            self.send_html('index_get.html')
        elif real_path == '/post':
            self.send_html('index_post.html')
        elif real_path == '/button':
            self.proc_query()
        elif real_path == '/form_get':
            self.proc_query()
        elif real_path == '/form_post':
            self.proc_form_post()
        else:
            self.response(404, '<h1>Not Found</h1>')
        
    def send_html(self, filename):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'r', encoding='utf-8') as f:
            msg = f.read()
            self.wfile.write(msg.encode()) # 본문 전송
        
    def proc_query(self):
        parsed_path = parse.urlparse(self.path)
        query = parsed_path.query
        print(query)
        parsed_query = parse.parse_qs(query) # 쿼리 status=on을 {'status': ['on']}으로 파싱
        print(parsed_query)
        status = parsed_query['status'][0]
        if status == 'on':
            message = '<h2>LED in IoT Device is now turned on</h2>'
        #GP.output(18, 1) # 라즈베리파이 LED 제어 코드
        elif status == 'off':
            message = '<h2>LED in IoT Device is now turned off</h2>'
        #GP.output(18, 0) # 라즈베리파이 LED 제어 코드
        else:
            message = '<h2>Wrong status</h2>'
        self.response(200, message)
        
    def proc_form_post(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode() # HTTP Request의 body 읽기
        print(body) # body 내용은 쿼리 status=on(또는 off)
        parsed_body = body.split('=') # parsed_body = ['status', 'on']
        print(parsed_body)
        status = parsed_body[1]
        if status == 'on':
            message = '<h2>LED in IoT Device is now turned on</h2>'
        #GP.output(18, 1) # 라즈베리파이 LED 제어 코드
        elif status == 'off':
            message = '<h2>LED in IoT Device is now turned off</h2>'
        #GP.output(18, 0) # 라즈베리파이 LED 제어 코드
        else:
            message = '<h2>Wrong status</h2>'
        self.response(200, message)
        
    def response(self, status_code, body): # 응답 메시지 전송 함수
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(body.encode())

httpd = HTTPServer(('localhost', 8080), http_handler)
print('Serving HTTP on {}:{}'.format('localhost', 8080))
httpd.serve_forever()