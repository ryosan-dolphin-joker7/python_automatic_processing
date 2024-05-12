import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import gmail_send # 前節で作ったモジュール
import my_gmail_account as gmail # アカウント情報

# メールデータを作成 --- (*1)
msg = MIMEMultipart()
msg['Subject'] = '富士山の写真'
msg['From'] = gmail.account
msg['To'] = gmail.account
# テキストを追加 --- (*2)
txt = MIMEText('先日ドライブに行った時に撮影した写真です。' + \
        'ご査収ください。')
msg.attach(txt)
# 画像を添付 --- (*3)
with open('sky.jpg', 'rb') as fp:
    img = MIMEImage(fp.read())
    msg.attach(img)

# メール送信 --- (*4)
gmail_send.send_gmail(msg)
print("ok")
