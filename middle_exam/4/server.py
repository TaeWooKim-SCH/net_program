# ex3_webserver.py - 기출 3번 (15점)
# 기존 과제5 웹 서버 기능 + /exam?q=문자열 쿼리 처리
# 브라우저에 <h1>Hello, 문자열</h1> HTML 응답

from socket import *
from urllib.parse import unquote

s = socket()
s.bind(('', 80))
s.listen(10)
print('Web server running on port 80...')

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    if not data:
        c.close(); continue

    msg = data.decode(errors='ignore')
    req = msg.split('\r\n')
    parts = req[0].split(' ')
    if len(parts) < 2:
        c.close(); continue
    url = parts[1]                        # '/exam?q=hello' 또는 '/index.html'

    # --- 1) 쿼리 문자열 분리 ---
    if '?' in url:
        path_part, query = url.split('?', 1)
    else:
        path_part, query = url, ''

    filename = path_part[1:]              # 맨 앞 '/' 제거
    if filename == '':
        filename = 'index.html'

    # --- 2) midterm 경로 처리 (추가 기능) ---
    if filename == 'midterm':
        params = {}
        for pair in query.split('&'):
            if '=' in pair:
                k, v = pair.split('=', 1)
                params[k] = unquote(v)
        name = params.get('name', '')
        id = params.get('id', '')
        body = '<html><body><h1>Hello, ' + name + "! Your ID is " + id + '</h1></body></html>'
        header = ('HTTP/1.1 200 OK\r\n'
                  'Content-Type: text/html; charset=utf-8\r\n\r\n')
        c.send(header.encode())
        c.send(body.encode('utf-8'))
        c.close(); continue

    # --- 3) 기존 기능 (index.html, iot.png, favicon.ico) ---
    try:
        if filename == 'index.html':
            mimeType = 'text/html; charset=utf-8'
            f = open(filename, 'r', encoding='utf-8')
            body = f.read(); f.close()
            header = ('HTTP/1.1 200 OK\r\n'
                      'Content-Type: ' + mimeType + '\r\n\r\n')
            c.send(header.encode())
            c.send(body.encode())
        elif filename == 'iot.png':
            mimeType = 'image/png'
            f = open(filename, 'rb')
            body = f.read(); f.close()
            c.send(('HTTP/1.1 200 OK\r\n'
                    'Content-Type: ' + mimeType + '\r\n\r\n').encode())
            c.send(body)
        elif filename == 'favicon.ico':
            mimeType = 'image/x-icon'
            f = open(filename, 'rb')
            body = f.read(); f.close()
            c.send(('HTTP/1.1 200 OK\r\n'
                    'Content-Type: ' + mimeType + '\r\n\r\n').encode())
            c.send(body)
        else:
            raise FileNotFoundError
    except:
        resp = ('HTTP/1.1 404 Not Found\r\n\r\n'
                '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
                '<BODY>Not Found</BODY></HTML>')
        c.send(resp.encode())
    c.close()
