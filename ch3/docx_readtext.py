import docx

# 既存Wordファイルを読み込む --- (*1)
doc = docx.Document('letter.docx')

# 段落を順次表示 --- (*2)
for p in doc.paragraphs:
    print(p.text)

