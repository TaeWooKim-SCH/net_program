# 메일 보내기: 여러 사람에게 메일 전송 + 이미지 파일 첨부하기

import os
import smtplib
import filetype # 파일 유형을 판단해주는 모듈
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = os.getenv('EMAIL_SENDER')
recipient = 'daeheekim@sch.ac.kr'
password = os.getenv('EMAIL_PASSWORD')
family = ['zop1234@hanamil.net', 'zop1234@sch.ac.kr', 'tobestar29@naver.com']

msg = EmailMessage()
msg['Subject'] = '우리 가족 사진'
msg['From'] = sender # 보내는 사람: sender's email address
msg['To'] = ', '.join(family) # 받는 사람: family 리스트에 있는 모든 email addresses
msg.set_content('우리 가족의 행복한 사진입니다.')

# 첨부할 파일 열기
with open('profile.jpeg', 'rb') as f:
    img_data = f.read()

# add_attachment 함수를 이용해 파일 첨부. 파일 첨부시 첨부된 파일의 mime-type 지정
msg.add_attachment(img_data, maintype='image', subtype=filetype.guess_mime(img_data), filename='test.jpg')

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()