import socket
import threading

PORT = 5000
BUFSIZE = 1024

sharedData = {}

def thread_handler(sock: socket.socket):
    while (True):
        global sharedData, lock

        data = sock.recv(BUFSIZE)
        decoded_data = data.decode()
        device_name, temp, humidity = decoded_data.split(" ")
        lock.acquire()
        sharedData[device_name].append({
            "temp": int(temp),
            "humidity": int(humidity)
        })
        print(sharedData)
        lock.release()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', PORT))
sock.listen(5)

lock = threading.Lock()

while (True):
    client, address = sock.accept()
    data = client.recv(BUFSIZE)

    lock.acquire()
    sharedData[data.decode()] = []
    lock.release()

    print('connected by', address)
    th = threading.Thread(target=thread_handler, args=(client,))
    th.start()
