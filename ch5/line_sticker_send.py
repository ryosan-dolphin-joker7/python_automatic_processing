import requests

# アクセストークンを以下に設定★ --- (*1)
acc_token = 'lmHI5oxoGSN2f5YU79tyrVuhiAp1QWJHpKlW1YSjOzO'

def send_sticker_line(msg, package_id, sticker_id):
    # サーバーに送るパラメータを用意 --- (*2)
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {
        'message': msg,
        'stickerPackageId': package_id,
        'stickerId': sticker_id,
        }
    # サーバーへ送信 --- (*3)
    requests.post(url, headers=headers, params=payload)

if __name__ == '__main__':
    send_sticker_line('スタンプ付きで、こんにちは', 4, 303)
    print('ok')
