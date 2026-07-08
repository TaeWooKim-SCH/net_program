# 변형 1 — 명령 실행 결과를 메일 "본문"에 담기 (가장 유력)
# invoke_shell은 프롬프트·명령어 에코까지 섞여 들어오는데,
# exec_command는 결과(stdout)만 깔끔하게 줌
import os, getpass, smtplib, paramiko
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

# --- SSH로 명령 실행 후 결과 수집 ---
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
user = input('Username: ')
pwd = getpass.getpass('Password: ')
ssh.connect('114.71.220.5', 22, username=user, password=pwd)

stdin, stdout, stderr = ssh.exec_command('cat /proc/cpuinfo')
cpu_info = stdout.read().decode()
stdin, stdout, stderr = ssh.exec_command('cat /proc/meminfo')
mem_info = stdout.read().decode()
ssh.close()

# --- 결과를 본문에 담아 메일 전송 ---
msg = EmailMessage()
msg['Subject'] = '20211483 시스템 정보'
msg['From'] = os.getenv('EMAIL_SENDER')
msg['To'] = 'zop1234@sch.ac.kr' # 시험때 꼭 교수님 메일로 바꿔야 함
msg.set_content(f'[CPU 정보]\n{cpu_info}\n\n[메모리 정보]\n{mem_info}')   # 본문에 결과

s = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
s.ehlo(); s.starttls()
s.login(os.getenv('EMAIL_SENDER'), os.getenv('EMAIL_PASSWORD'))
s.send_message(msg)
s.quit()



# 변형 2 — SFTP 방향 뒤집기 (다운로드 → 업로드)
# sftp = ssh.open_sftp()
# sftp.put('iot.png', '/home/user/iot.png')   # 로컬 → 원격 (get의 반대)
# sftp.close()

# 변형 3 — 첨부 형태 바꾸기
# # 여러 파일 각각 첨부
# for fname, mtype, stype in [('iot.png', 'image', 'png'),
#                             ('result.txt', 'text', 'plain'),
#                             ('data.zip', 'application', 'zip')]:
#     with open(fname, 'rb') as f:
#         msg.add_attachment(f.read(), maintype=mtype, subtype=stype, filename=fname)

# 변형 4 — 스크래핑 추출 결과를 파일로 저장하거나 메일로 전송 (C와 결합)
# import re
# emails = re.findall(r'[\w.]+@[\w.]+\.[a-z]{2,3}', html)

# # 파일로 저장
# with open('emails.txt', 'w', encoding='utf-8') as f:
#     for e in emails:
#         f.write(e + '\n')