import smtplib, ssl
from email.mime.text import MIMEText
import my_yahooj_account as yahooj # アカウント情報

# メイン処理 --- (*1)
def send_test_email():
    # メールデータ(MIME)を作成
    msg = make_mime_text(
        mail_to=yahooj.account,
        subject='メールの送信テスト',
        body='こんにちは。届きましたか？テストテスト。')
    # メール送信
    send_yahooj_mail(msg)

# メールデータ(MIME)を生成する --- (*2)
def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, 'plain')
    msg['Subject'] = subject     # 件名
    msg['To'] = mail_to          # 宛先
    msg['From'] = yahooj.account # 送信元
    return msg

# Yahoo!メールに接続 --- (*3)
def send_yahooj_mail(msg):
    # Yahoo!メールのサーバーに接続 --- (*4)
    server = smtplib.SMTP_SSL(
        'smtp.mail.yahoo.co.jp', 465,
        context=ssl.create_default_context())
    # ログインしてメールを送信
    server.login(
        yahooj.account,
        yahooj.password)
    server.send_message(msg)

if __name__ == '__main__':
    send_test_email()
    print('ok.')

