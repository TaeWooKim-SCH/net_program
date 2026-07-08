import socket
import cv2
import numpy as np

BUF_SIZE = 8192
LENGTH = 10
videoFile = 'test.mp4'

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(('', 5000))
tcp_socket.listen(5)

while (True):
  client, address = tcp_socket.accept()
  print('Client is connected')
  cap = cv2.VideoCapture(videoFile)

  while (cap.isOpened()):
    ret, frame = cap.read()
    if (ret):
      temp = client.recv(BUF_SIZE) # 'start' 수신
      if (not temp):
        break

      result, imgEncode = cv2.imencode('.jpg', frame)
      data = np.array(imgEncode)
      byteData = data.tobytes()
      client.send(str(len(byteData)).zfill(LENGTH).encode()) # 10개 문자열로 표현된 길이 전송

      temp = client.recv(BUF_SIZE)
      if (not temp):
        break

      client.send(byteData) # 이미지 데이터 전송
    else:
      break

  cap.release()
  cv2.destroyAllWindows()
  client.close()