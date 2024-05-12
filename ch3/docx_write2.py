import docx
import datetime

template_file = 'letter.docx'
save_file = 'letter-suzuki2.docx'
now = datetime.datetime.now()

# 書き換える内容を指定
card = {
  '2021年10月10日': now.strftime('%Y年%m月%d日'),
  '●●●御中': 'マイナビ出版御中',
  '■■■様': '鈴木様',
  '★★★の送付について': '契約書の送付について'
}
# どの部分に書式を設定するか --- (*1)
cstyle = {
  '★★★の送付について': True
}

# Wordファイルを開く
doc = docx.Document(template_file)

# 内容を書き換える
for p in doc.paragraphs:
    # テキストを書き換え --- (*2)
    for k,v in card.items():
        if p.text.find(k) >= 0:
            p.text = p.text.replace(k, v)
            # 書式を設定するか？ --- (*3)
            if k in cstyle:
                font = p.runs[0].font
                font.bold = True
                font.underline = True
                font.size = docx.shared.Pt(20)

# Wordファイルへ保存
doc.save(save_file)


