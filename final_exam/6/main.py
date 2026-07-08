# SSH: 원격 시스템에서 연속적으로 명령어 실행하기

import os
import getpass
import paramiko
import smtplib
import time
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input('Username: ')
pwd = getpass.getpass('Password: ')
ssh.connect('114.71.220.5', 22, username=user, password=pwd)

channel = ssh.invoke_shell() # 새로운 셸 세션(channel) 생성

# 1 ~ 3 번
channel.send('mkdir -p 20211483\n')
time.sleep(0.5)
channel.send('cd 20211483\n')
time.sleep(0.5)
channel.send('echo iot > iot.txt\n')
time.sleep(0.5)
channel.send('cat /proc/meminfo > mem.txt\n')
time.sleep(0.5)


# 4번
sftp = ssh.open_sftp()

src_file_path = 'net_program.txt'
dst_file_path = '/home/net_pro/20211483/' + src_file_path
sftp.put(src_file_path, dst_file_path)

# 5 ~ 6번
# ssh 통해 생성 후 zip 압축
filename = '20211483.zip' # 압축파일의 이름
dirname = '20211483' # 압축할 폴더
zip_command = 'zip -r ' + filename + ' ' + dirname # 리눅스 압축 명령어

channel.send('cd ~\n')
time.sleep(0.5)
channel.send(f'{zip_command}\n')
time.sleep(0.5)

# 로컬로 가져오기
sftp = ssh.open_sftp()
sftp.get(filename, filename)

ssh.close()

# 7
# 이메일 전송
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# 송신자, 수신자, 비밀번호
sender = os.getenv('EMAIL_SENDER')
recipient = 'daeheekim@sch.ac.kr'
password = os.getenv('EMAIL_PASSWORD')

# 메시지 생성하기
msg = EmailMessage()
msg['Subject'] = '네트워크 프로그래밍 기말고사 6번'
msg['From'] = sender
msg['To'] = recipient
text = '네트워크 프로그래밍 기말고사 6번 답안 제출합니다.'
msg.set_content(text)

# 첨부할 파일 열기
with open(filename, 'rb') as f:
    file_data = f.read()
msg.add_attachment(file_data, maintype='application', subtype='zip', filename='final.zip')

# SMTP 객체 생성 후, 메시지 전송
s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()
