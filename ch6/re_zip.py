import re

# データファイルを読み出し --- (*1)
with open('address.txt', 'rt', encoding='utf-8') as f:
    text = f.read()

# 正規表現で取得 --- (*2)
a = re.findall(r'〒\d{3}-\d{4}', text)
print(a)
