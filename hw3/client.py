import socket;
import json;

port = 8080;
address = ("localhost", port);
BUFSIZE = 1024;
ENCODING_FORMAT = 'utf-8';

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.connect(address);

while True:
  msg = input("계산식을 작성해주세요(더하기, 뺴기, 곱셈 나눗셈): ");
  
  if (msg == 'q'):
    break;
  
  try:
    bytesSend = s.send(msg.encode(ENCODING_FORMAT));
  except:
    print("connection closed");
    break;

  try:
    data = s.recv(BUFSIZE).decode(ENCODING_FORMAT);
    if (not data):
      break;

    parsed_data = json.loads(data);
    if (parsed_data["status"] == 0):
      print("계산 결과: {0}".format(parsed_data["value"]));
    elif (parsed_data["status"] == 1):
      print(parsed_data["message"]);
    else:
      print(parsed_data["message"]);
      break;

  except:
    print("connection closed");
    break;

s.close();
