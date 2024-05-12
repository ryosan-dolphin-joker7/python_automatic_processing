import requests
# URL
check_url = 'https://api.aoikujira.com/ip/ini'

# User-Agentを指定
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'

# (1) User-Agentを指定しない場合
res = requests.get(check_url)
print(res.text)

# (2) User-Agentを指定した場合
headers = {'user-agent': ua} # ヘッダを指定
res = requests.get(check_url, headers=headers)
print(res.text)

