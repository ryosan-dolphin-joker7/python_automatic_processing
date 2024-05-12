import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail # アカウント情報
import gmail_send # さっき作ったプログラム

# 本文のHTMLを指定 --- (*1)
html = '''
    <html><meta charset="utf-8"><body>
    <h1>HTMLメールを送れます</h1>
    <p>仕事に役立つ格言</p>
    <ul>
      <li>最も重要な決定とは、何をするかではなく、
        何をしないかを決めることだ(スティーブジョブズ)</li>
      <li>人から批判されることを恐れてはならない。
        それは成長の肥やしとなる(トーマスエジソン)</li>
      <li>良い名は多くの富に勝る(格言)</li>
    </ul>
    </body></html>
'''
# メールデータをHTMLで作成 --- (*2)
msg = gmail_send.make_mime_text(
    mail_to=gmail.account,
    subject='HTMLメールの送信テスト',
    body=html)
# メール送信 --- (*3)
gmail_send.send_gmail(msg)
print("ok")
