import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail # アカウント情報
import gmail_send # さっき作ったプログラム

# メールデータを作成 --- (*1)
msg = MIMEText('こんにちは。CCのテストでみんなに送っています！')
msg['Subject'] = 'CCのテスト'
msg['To'] = gmail.account
msg['From'] = gmail.account
msg['Cc'] = gmail.account
# msg['Bcc'] = ''
msg.add_header('reply-to', 'test@example.com') # --- (*1a)

# メール送信 --- (*2)
gmail_send.send_gmail(msg)
print("ok")
