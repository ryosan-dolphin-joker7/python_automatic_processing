import chardet, requests

# 青空文庫 > 走れメロス
url = 'https://www.aozora.gr.jp/cards/000035/files/1567_14913.html'
# バイナリとしてダウンロード --- (*1)
bindata = requests.get(url).content
# 文字エンコーディングを判定 --- (*2)
r = chardet.detect(bindata)
# 結果を表示
print(r)
