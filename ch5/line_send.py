import requests

# アクセストークンを以下に設定★ --- (*1)
acc_token = 'lmHI5oxoGSN2f5YU79tyrVuhiAp1QWJHpKlW1YSjOzO'

def send_line(msg):
    # サーバーに送るパラメータを用意 --- (*2)
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}
    requests.post(url, headers=headers, params=payload)

if __name__ == '__main__':
    # メッセージを送信 --- (*3)
    send_line('Pythonからこんにちは！')
    print('ok')
