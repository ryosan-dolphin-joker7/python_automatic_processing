import tkinter as tk
import tkinter.messagebox as mb

# ウィンドウを隠す --- (*1)
tk.Tk().withdraw()

# 二択ボックスを表示 --- (*2)
yesno = mb.askyesno('質問', '処理を実行しますか？')

# ユーザーの回答により動作を変更する --- (*3)
if yesno:
    mb.showinfo('はいを選択', '処理を実行しました')
else:
    mb.showinfo('いいえを選択', '実行しませんでした')

