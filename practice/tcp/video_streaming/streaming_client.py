import socket
import cv2
import numpy as np

BUF_SIZE = 8192
LENGTH = 10

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(('localhost', 5000))

while (True):
  tcp_socket.send(b'start')

  rx_size = 0
  data = b''
  while (rx_size < LENGTH):
    rx_buf = tcp_socket.recv(BUF_SIZE)
    if (not rx_buf):
      break

    data = data + rx_buf
    rx_size += len(rx_buf)

  if (rx_size < LENGTH):
    break

  frame_len = int(data)

  tcp_socket.send(b'image')

  rx_size = 0
  byteData = b''
  while (rx_size < frame_len):
    rx_buf = tcp_socket.recv(BUF_SIZE)
    if (not rx_buf):
      break
    
    byteData = byteData + rx_buf
    rx_size += len(rx_buf)

  if (rx_size < frame_len):
    break

  data = np.frombuffer(byteData, dtype='uint8')
  imgDecode = cv2.imdecode(data, 1)
  cv2.imshow('image', imgDecode)

  if (cv2.waitKey(1) & 0xFF == ord('q')):
    break

tcp_socket.close()