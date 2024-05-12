import docx
import datetime

template_file = 'letter.docx'
save_file = 'letter-suzuki.docx'
now = datetime.datetime.now()

# 書き換える内容を指定 --- (*1)
card = {
  '2021年10月10日': now.strftime('%Y年%m月%d日'),
  '●●●御中': 'マイナビ出版御中',
  '■■■様': '鈴木様',
  '★★★の送付について': '契約書の送付について'
}

# Wordファイルを開く --- (*2)
doc = docx.Document(template_file)

# 内容を書き換える --- (*3)
for p in doc.paragraphs:
    # テキストを書き換え --- (*4)
    for k,v in card.items():
        if p.text.find(k) >= 0:
            p.text = p.text.replace(k, v)

# Wordファイルへ保存 --- (*5)
doc.save(save_file)


