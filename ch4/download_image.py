import requests

# 画像ファイルのURL
url = 'https://uta.pw/shodou/img/3/3.png'

# URLのリソースを取得 --- (*1)
res = requests.get(url)

# 戻り値をチェック --- (*2)
if not res.ok:
    print("失敗:", res.status_code)
    quit()

# ファイルに保存 --- (*3)
with open('gyudon.png', 'wb') as fp:
    fp.write(res.content)
print("ok.")
