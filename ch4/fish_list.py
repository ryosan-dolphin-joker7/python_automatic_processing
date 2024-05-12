from bs4 import BeautifulSoup

# HTMLファイルを読んでBeautifulSoupで解析 --- (*1)
with open('fish.html',encoding='utf-8') as fp:
  html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

# CSSセレクタで魚の一覧を得る --- (*2)
res = []
div_list = soup.select('#fishes > div')
for div in div_list:
    # divの子要素にあるh2を得る --- (*3)
    fish = div.h2.text
    # さらにCSSセレクタで検索 --- (*4)
    desc = div.select('.desc')[0].text
    price = div.select('.price')[0].text
    print(fish, desc, price)
    # 結果をリストに追加 --- (*5)
    res.append([fish, desc, price])

# CSVに変換して保存 --- (*6)
import csv
with open('fish.csv', 'wt', encoding='sjis', newline='') as fp:
    csv.writer(fp).writerows(res)
