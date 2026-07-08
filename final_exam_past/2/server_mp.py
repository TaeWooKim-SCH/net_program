# 풀 방식
import socket
from multiprocessing import Process

PORT = 8888
BUFSIZE = 1024

def processClient(c_sock):
    try:
        data = c_sock.recv(BUFSIZE)
        msg = data.decode(errors='ignore')
        req = msg.split("\r\n")

        request_line = req[0].split(" ")
        target = request_line[1]
        print(f'요청된 경로: {target}')

        if target == '/':
            with open('iot.png', 'rb') as f:
                file_data = f.read()
            header = "HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n".encode('utf-8')
            c_sock.sendall(header + file_data)
        else:
            header = "HTTP/1.1 404 Not Found\r\n\r\n".encode('utf-8')
            body = "<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>".encode('utf-8')
            c_sock.sendall(header + body)
    except Exception as error:
        print(f"서버 에러 발생: {error}")
    finally:
        c_sock.close()

def worker(sock):
    while True:
        client, addr = sock.accept()    # 여러 프로세스가 같은 소켓에서 경쟁적으로 accept
        processClient(client)

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', PORT))
    sock.listen(10)
    print(f'{PORT}번 포트에서 서버 열림')

    workers = [Process(target=worker, args=(sock,)) for _ in range(4)]
    for w in workers:
        w.start()
    for w in workers:
        w.join()

# 정석 - 오류 발생 위험 높음
# import socket
# from multiprocessing import Process

# PORT = 8888
# BUFSIZE = 1024

# def processClient(c_sock: socket.socket):
#     try:
#         data = c_sock.recv(BUFSIZE)
#         msg = data.decode(errors='ignore')
#         req = msg.split("\r\n")

#         request_line = req[0].split(" ")
#         target = request_line[1]
#         print(f'요청된 경로: {target}')

#         if target == '/':
#             with open('iot.png', 'rb') as f:
#                 file_data = f.read()
#             header = "HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n".encode('utf-8')
#             c_sock.sendall(header + file_data)
#         else:
#             header = "HTTP/1.1 404 Not Found\r\n\r\n".encode('utf-8')
#             body = "<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>".encode('utf-8')
#             c_sock.sendall(header + body)
#     except Exception as error:
#         print(f"서버 에러 발생: {error}")
#     finally:
#         c_sock.close()


# if __name__ == '__main__':                  # ★ 멀티프로세싱은 이 가드가 필수
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     sock.bind(('', PORT))
#     sock.listen(10)
#     print(f'{PORT}번 포트에서 서버 열림')

#     while True:
#         client, addr = sock.accept()
#         p = Process(target=processClient, args=(client,))   # 스레드 → 프로세스
#         p.start()