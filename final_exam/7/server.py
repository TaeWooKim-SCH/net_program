from http.server import HTTPServer, BaseHTTPRequestHandler
import json

students = {}

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.get_students()
    
    def do_POST(self):
        self.post_student()
    
    def get_students(self):
        self.response(200, students)
    
    def post_student(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode()
        json_body = json.loads(body)

        for key, value in json_body.items():
            students[key] = value
    
    def get_notfound(self):
        self.response(404, 'Not Found')

    def response(self, status_code, body):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body).encode())

httpd = HTTPServer(('localhost', 8000), http_handler)
print('Serving HTTP on {}:{}'.format('localhost', 8000))
httpd.serve_forever()