from http.server import HTTPServer, BaseHTTPRequestHandler

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        with open('index.html', 'r', encoding='utf-8') as f:
            msg = f.read()
            self.wfile.write(msg.encode())

httpd = HTTPServer(('localhost', 8080), http_handler)
print('Serving HTTP on {}:{}'.format('localhost', 8080))
httpd.serve_forever()