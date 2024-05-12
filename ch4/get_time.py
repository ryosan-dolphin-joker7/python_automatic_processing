# requestsモジュールを取り込む --- (*1)
import requests

# 現在時刻を提供しているサーバーにアクセス --- (*2)
url = 'https://api.aoikujira.com/time/get.php'
result = requests.get(url)
# 結果を表示 --- (*3)
print(result.text) 


