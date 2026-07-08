import socket
import threading

PORT = 8888
BUFSIZE = 1024

def sendTask(c_sock: socket.socket):
    with open('iot.png', 'rb') as f:
        file_data = f.read();

        content_type = f"Content-Type: image/png";
        header = f"HTTP/1.1 200 OK\r\n{content_type}; charset=utf-8\r\n\r\n".encode('utf-8');
        c_sock.send(header + file_data);
        

sock = socket.socket();
sock.bind(('', 80));
sock.listen(10);
print('80번 포트에서 서버 열림')

while True:
    client, addr = sock.accept();

    try:
        data = client.recv(BUFSIZE);
        msg = data.decode();
        req = msg.split("\r\n");

        # 웹 서버 코드 작성
        # 각 객체(파일 또는 문자열) 전송 후, 소켓 닫기(c.close())
        request_line = req[0].split(" ");
        if len(request_line) < 3: # 가끔 브라우저가 빈 요청 보내는 것 방지
            continue;

        method = request_line[0];
        target = request_line[1];
        http_version = request_line[2];

        print(f'요청된 경로: {target}');
        # /index
        if (target.startswith('/index')):
            with open('index.html', 'rb') as f:
                file_data = f.read();

            content_type = f"Content-Type: text/html";
            header = f"HTTP/1.1 200 OK\r\n{content_type}; charset=utf-8\r\n\r\n".encode('utf-8');
            client.send(header + file_data);
    
        # /iot
        elif (target.startswith('/')):
            with open('iot.png', 'rb') as f:
                file_data = f.read();
          
            content_type = f"Content-Type: image/png";
            header = f"HTTP/1.1 200 OK\r\n{content_type}; charset=utf-8\r\n\r\n".encode('utf-8');
            client.send(header + file_data);
    
        # /favicon
        elif (target.startswith('/favicon')):
            with open('favicon.ico', 'rb') as f:
                file_data = f.read();

            content_type = f"Content-Type: image/x-icon";
            header = f"HTTP/1.1 200 OK\r\n{content_type}; charset=utf-8\r\n\r\n".encode('utf-8');
            client.send(header + file_data);
    
        # /exam
        elif (target.startswith('/exam')):
            query = target.split('?');
            name = query[1] if len(query) > 1 else "Guest";

            content_type = f"Content-Type: text/html";
            header = f"HTTP/1.1 200 OK\r\n{content_type}; charset=utf-8\r\n\r\n".encode('utf-8');
            body = f"Hello, {query[1]}".encode('utf-8');
            client.send(header + body);
  
        # 404 Not Found
        else:
            header = "HTTP/1.1 404 Not Found\r\n\r\n".encode('utf-8');
            body = "<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>".encode('utf-8');
            client.send(header + body);
    except Exception as error:
        print(f"서버 에러 발생: {error}");
        header = "HTTP/1.1 500 Internal Server Error\r\n\r\n".encode('utf-8');
        body = "<HTML><HEAD><TITLE>Internal Server Error</TITLE></HEAD><BODY>500 Internal Server Error</BODY></HTML>".encode('utf-8');
        client.send(header + body);
    finally:
        client.close();
