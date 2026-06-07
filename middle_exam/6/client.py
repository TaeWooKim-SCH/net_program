import socket
import random

# 서버 주소 및 포트 설정
server_ip = '127.0.0.1' # 로컬 테스트용 (필요 시 서버 IP로 변경)
port = 3333
BUFF_SIZE = 1024

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (server_ip, port)

while True:
  # ==========================================
  # 1. 메시지 송신 부분 (클라이언트 -> 서버)
  # ==========================================
  msg = input('-> ')
  reTx = 0 # 재전송 횟수 초기화
  
  # 'ack' 응답 메시지를 수신하지 못하는 경우, 1초 간격으로 최대 3회 재전송 (총 4회)
  while reTx <= 3:
    # 재전송 횟수와 메시지를 결합하여 전송
    resp = str(reTx) + ' ' + msg
    sock.sendto(resp.encode(), server_addr)
    
    sock.settimeout(1) # 1초 간격 재전송을 위한 소켓 타임아웃 1초 설정
    
    try:
      # 서버로부터 'ack' 대기
      data, addr = sock.recvfrom(BUFF_SIZE)
    except socket.timeout:
      # 타임아웃(2초) 발생 시 재전송 횟수 1 증가시키고 다시 시도
      reTx += 1
      continue
    else:
      # 정상적으로 'ack'를 받으면 송신 루프 종료
      break

  # ==========================================
  # 2. 메시지 수신 처리 부분 (서버 -> 클라이언트)
  # ==========================================
  sock.settimeout(None)  # 메시지 수신을 위해 소켓 블로킹 모드(무한정 대기)로 설정
  
  while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    
    # 메시지 수신 후, 30% 확률로 응답하지 않음 (고의로 메시지 손실 만듦)
    if random.random() <= 0.3:
      continue
    else:
      # 손실되지 않은 경우 'ack' 응답을 보내고, 화면에 채팅 메시지 출력
      sock.sendto(b'ack', addr)
      print('<-', data.decode())
      break