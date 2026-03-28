import socket;
import json;

port = 8080;
BUFSIZE = 1024;
ENCODING_FORMAT = 'utf-8';

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
sock.bind(('', port));
sock.listen(1);


while True:
  client, addr = sock.accept();

  while True:
    try:
      msg = client.recv(BUFSIZE).decode(ENCODING_FORMAT);
      if (not msg):
        break;
      
      parsed_msg = msg.replace(" ", "");
      data = {
        "status": 0, # 0: 정상, 1: 미지원 연산, 2: 오류
        "message": "성공적으로 처리되었습니다."
      };

      if ("+" in parsed_msg):
        split_msg = parsed_msg.split("+");
        data["value"] = int(split_msg[0]) + int(split_msg[1]);
      elif ("-" in parsed_msg):
        split_msg = parsed_msg.split("-");
        data["value"] = int(split_msg[0]) - int(split_msg[1]);
      elif ("*" in parsed_msg):
        split_msg = parsed_msg.split("*");
        data["value"] = int(split_msg[0]) * int(split_msg[1]);
      elif ("/" in parsed_msg):
        split_msg = parsed_msg.split("/");
        data["value"] = int(split_msg[0]) / int(split_msg[1]);
      else:
        data["status"] = 1;
        data["message"] = "지원하지 않는 연산자이거나 연산자가 존재하지 않습니다. 다시 시도해주세요";
      
      message = json.dumps(data).encode(ENCODING_FORMAT);
      client.sendall(message);
    
    except Exception as error:
      print(error);
      data["status"] = 2;
      data["message"] = "서버 오류 발생. 연결을 종료합니다.";
      message = json.dumps(data).encode(ENCODING_FORMAT);
      client.sendall(message);
      break;

  client.close();
