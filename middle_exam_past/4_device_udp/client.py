import socket;

def run_client():
  # UDP 소켓 생성
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
  server_address = ('localhost', 8000);

  # 무한 반복
  while (True):
    request = input("\n요청할 정보 번호 (1: 온도, 2: 습도, 3: 조도): ").strip();

    if (request.lower() == 'q'):
      break;

    if (request not in ['1', '2', '3']):
      print("잘못된 입력입니다. 1, 2, 3 중 하나를 입력하세요.");
      continue;

    # 서버로 문자열 전송 ('1', '2', '3')
    udp_socket.sendto(request.encode('utf-8'), server_address);

    # 서버로부터 데이터 수신 (항상 6바이트가 와야 함)
    data, _ = udp_socket.recvfrom(1024);

    if (len(data) == 6):
      # 수신된 6바이트를 2바이트씩 잘라서 빅 엔디언으로 파싱 (역직렬화)
      print(data);
      temp = int.from_bytes(data[0:2], byteorder='big', signed=True);
      humid = int.from_bytes(data[2:4], byteorder='big', signed=True);
      lumi = int.from_bytes(data[4:6], byteorder='big', signed=True);

      # 문제 형식에 맞춰 출력
      print(f"Temp={temp}, Humid={humid}, Lumi={lumi}");
    else:
      print("서버로부터 6바이트가 아닌 데이터가 수신되었습니다.")

  udp_socket.close();

if (__name__ == "__main__"):
  run_client();

