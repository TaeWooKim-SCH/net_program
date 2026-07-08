import socket
import threading

PORT = 8888
BUFSIZE = 1024

def processClient(c_sock: socket.socket):
    try:
        data = c_sock.recv(BUFSIZE)
        msg = data.decode()
        req = msg.split("\r\n")

        # 웹 서버 코드 작성
        # 각 객체(파일 또는 문자열) 전송 후, 소켓 닫기(c.close())
        request_line = req[0].split(" ")
        target = request_line[1]

        print(f'요청된 경로: {target}')
    
        # /
        if (target == '/'):
            with open('iot.png', 'rb') as f:
                file_data = f.read()
          
            header = f"HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n".encode('utf-8')
            c_sock.send(header + file_data)
  
        # 404 Not Found
        else:
            header = "HTTP/1.1 404 Not Found\r\n\r\n".encode('utf-8')
            body = "<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>".encode('utf-8')
            c_sock.send(header + body)
    except Exception as error:
        print(f"서버 에러 발생: {error}")
        header = "HTTP/1.1 500 Internal Server Error\r\n\r\n".encode('utf-8')
        body = "<HTML><HEAD><TITLE>Internal Server Error</TITLE></HEAD><BODY>500 Internal Server Error</BODY></HTML>".encode('utf-8')
        c_sock.send(header + body)
    finally:
        c_sock.close()
        

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', PORT))
sock.listen(10)
print(f'{PORT}번 포트에서 서버 열림')

while True:
    client, addr = sock.accept();

    th = threading.Thread(target=processClient, args=(client,))
    th.start()
