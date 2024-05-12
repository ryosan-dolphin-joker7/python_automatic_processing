from bs4 import BeautifulSoup

# HTMLファイルを読む --- (*1)
with open('fish.html',encoding='utf-8') as fp:
  html_str = fp.read()

# Beautiful Soupのオブジェクト作成 --- (*2)
soup = BeautifulSoup(html_str, 'html5lib')

# title要素を探して表示 --- (*3)
title = soup.find('title')
print(title)
