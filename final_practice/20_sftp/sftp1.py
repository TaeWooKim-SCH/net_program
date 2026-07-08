# SFTP 1: 파일 송수신 (Transport 이용)

import paramiko
import getpass

# 인증과 보안을 제공해주는 보안채널(Transport) 생성
transport = paramiko.Transport(('114.71.220.5', 22))

user = input('Username: ')
pwd = getpass.getpass('Password: ')
transport.connect(username=user, password=pwd)

# SFTP 클라이언트 객체 생성
sftp = paramiko.SFTPClient.from_transport(transport)

src_file_path = 'test/iot.txt'
dst_file_path = src_file_path.split('/')[1]
sftp.get(src_file_path, dst_file_path)

src_file_path = 'index.html'
dst_file_path = src_file_path
sftp.put(src_file_path, dst_file_path)

sftp.close()
transport.close()