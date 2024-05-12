from bs4 import BeautifulSoup

# HTMLファイルを読んでBeautifulSoupで解析
with open('fish.html',encoding='utf-8') as fp:
  html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

# CSSセレクタでウナギの値段を探す --- (*1)
p = soup.select('div#eel > p.price')
print(p[0].string)
