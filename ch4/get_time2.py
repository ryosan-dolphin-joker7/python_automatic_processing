import requests

# 現在時刻を提供しているサーバーにアクセス
url = 'https://api.aoikujira.com/time/get.php'
result = requests.get(url)
# アクセス結果を表示 --- (*1)
print("ok=", result.ok)
# アクセスに成功すれば取得したテキストを表示---(*2)
if result.ok:
    print("text=", result.text)
# ステータスコードを表示 --- (*3)
print("status_code=", result.status_code)


