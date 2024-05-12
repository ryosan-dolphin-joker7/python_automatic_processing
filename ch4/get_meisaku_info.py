import os, requests, csv
from bs4 import BeautifulSoup

# 名作作品のページ
target_url = 'https://uta.pw/shodou/index.php?master'
# TSVの保存パス
save_file = 'meisaku.txt'

# HTMLを取得してBeautiful Soupで解析 --- (*1)
html = requests.get(target_url).text
soup = BeautifulSoup(html, 'html5lib')

# CSSクエリで「.article」一覧を取得 --- (*2)
res = []
for art in soup.select('.article'):
    # 「.art_title」で絞り込み --- (*3)
    art_titles = art.select('.art_title')
    if len(art_titles) < 2: continue
    # 2つ目(0から数えて1)に実際の作品名と作者が入っている
    title = art_titles[1].text
    # ついでに画像URLも得る --- (*4)
    src = art.select('img')[0]['src']
    res.append([title, src])
    print(title, src)

# TSVをファイルに保存 --- (*5)
with open(save_file, 'wt', encoding='utf-8') as fp:
    csv.writer(fp, delimiter='\t').writerows(res)

