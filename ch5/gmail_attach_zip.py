import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import gmail_send # 前節で作ったモジュール
import my_gmail_account as gmail # アカウント情報

# メールデータを作成 --- (*1)
msg = MIMEMultipart()
msg['Subject'] = 'ZIPファイルの添付テスト'
msg['From'] = gmail.account
msg['To'] = gmail.account
# 本文テキストを追加 --- (*2)
txt = MIMEText('テストでZIPファイルを送ります。')
msg.attach(txt)
# ZIPファイルを添付 --- (*3)
zip_part = MIMEBase('application', 'zip') # ---(*3a)
with open('test.zip', 'rb') as fp: # --- (*3b)
    zip_part.set_payload(fp.read())
encoders.encode_base64(zip_part) # --- (*3c)
zip_part.add_header('Content-Disposition',
    'attachment', filename='test.zip') # --- (*3d)
msg.attach(zip_part)

# メール送信 --- (*4)
gmail_send.send_gmail(msg)
print("ok")
