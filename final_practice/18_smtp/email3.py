# 메일 보내기: 단체 메일 전송하기

import smtplib
from email.message import EmailMessage
from openpyxl import load_workbook

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'ninanooo@gmail.com'
password = '앱 비밀번호'

# 엑셀 파일 읽어오기
load_wb = load_workbook('email_list.xlsx')

# 워크시트 읽어오기
load_ws = load_wb['Sheet1']
for row in load_ws.rows:
    recipient = row[0].value

    msg = EmailMessage()
    msg['Subject'] = '휴강 공지'
    msg['From'] = sender
    msg.set_content('오늘 수업은 휴강입니다.')
    msg['To'] = recipient
    
    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.login(sender, password)
    s.send_message(msg)
    s.quit()