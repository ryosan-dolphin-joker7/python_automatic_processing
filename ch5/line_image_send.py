import requests

# アクセストークンを以下に設定★ --- (*1)
acc_token = 'lmHI5oxoGSN2f5YU79tyrVuhiAp1QWJHpKlW1YSjOzO'
# 画像ファイルのパスを指定
image_file = './sky.jpg'

def send_line(msg, image_file):
    # サーバーに送るパラメータを用意 --- (*2)
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}
    # 画像を読み込む --- (*3)
    with open(image_file, 'rb') as fp:
        files = {'imageFile': fp}
        # サーバーへ送信 --- (*4)
        requests.post(url, headers=headers, 
            params=payload, files=files)

if __name__ == '__main__':
    send_line('こんにちは', image_file)
    print('ok')
