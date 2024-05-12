import pyperclip

# クリップボードにコピー
pyperclip.copy('身勝手な人は自分の歩みの結果を刈り取る')

# クリップボードの内容を取得
text = pyperclip.paste()
print(text)

