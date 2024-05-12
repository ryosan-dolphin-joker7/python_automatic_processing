from bs4 import BeautifulSoup

# HTMLファイルを読んでBeautifulSoupで解析 --- (*1)
with open('fish.html',encoding='utf-8') as fp:
  html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

# h2の一覧を得る --- (*2)
for h2 in soup.find_all('h2'):
    # ウナギを調べる --- (*3)
    if h2.string == 'ウナギ':
        # 兄弟要素を調べる --- (*4)
        for e in h2.next_siblings:
            # p要素を調べる --- (*5)
            if e.name == 'p':
                # priceを探す --- (*6)
                if e['class'][0] == 'price':
                    print(e.string)
