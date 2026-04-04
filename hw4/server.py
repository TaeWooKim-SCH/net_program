import socket;

socket = socket.socket();
socket.bind(('', 80));
socket.listen(10);
print('80번 포트에서 서버 열림')

while True:
  client, addr = socket.accept();

  data = client.recv(1024);
  msg = data.decode();
  req = msg.split("\r\n");

  # 웹 서버 코드 작성
  # 각 객체(파일 또는 문자열) 전송 후, 소켓 닫기(c.close())
  request_line = req[0].split(" ");
  method = request_line[0];
  target = request_line[1][1:];
  http_version = request_line[2];
  mime_type_mapping = {
    'index.html': 'text/html',
    'iot.png': 'image/png',
    'favicon.ico': 'image/x-icon',
  };
  mime_type = mime_type_mapping.get(target);

  not_found_response = "HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>".encode('utf-8')
  server_error_response = "HTTP/1.1 500 Internal Server Error\r\n\r\n<HTML><HEAD><TITLE>Internal Server Error</TITLE></HEAD><BODY>500 Internal Server Error</BODY></HTML>".encode('utf-8')

  if (not mime_type):
    client.send(not_found_response);
  else:
    print(f'요청된 파일: {target}');
    try:
      with open(target, 'rb') as f:
        file_data = f.read();
      
      content_type_header = None;
      if (mime_type == 'text/html'):
        content_type_header = f"Content-Type: {mime_type}; charset=utf-8"
      else:
        content_type_header = f"Content-Type: {mime_type}";

      response_header = f"HTTP/1.1 200 OK\r\n{content_type_header}\r\n\r\n".encode('utf-8');
      client.send(response_header + file_data);
    except Exception as error:
      print(f"서버 에러 발생: {error}");
      client.send(server_error_response);
  client.close();
