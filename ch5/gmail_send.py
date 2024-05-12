import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail # アカウント情報 --- (*1)

# メイン処理 --- (*2)
def send_test_email():
    # メールデータ(MIME)を作成 --- (*3)
    msg = make_mime_text(
        mail_to=gmail.account,
        subject='メールの送信テスト',
        body='こんにちは。届きましたか？テストテスト。')
    # メール送信 --- (*4)
    send_gmail(msg)

# メールデータ(MIME)を生成する --- (*5)
def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject     # 件名
    msg['To'] = mail_to          # 宛先
    msg['From'] = gmail.account  # 送信元
    return msg

# Gmailに接続 --- (*6)
def send_gmail(msg):
    # Gmailサーバーに接続
    server = smtplib.SMTP_SSL(
        'smtp.gmail.com', 465,
        context=ssl.create_default_context())
    server.set_debuglevel(0) # ログ出力 --- (*7)
    # ログインしてメールを送信
    server.login(gmail.account, gmail.password)
    server.send_message(msg)

if __name__ == '__main__':
    send_test_email()
    print('ok.')

