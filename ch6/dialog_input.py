import tkinter as tk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd

# tkinterの窓を表示しない
tk.Tk().withdraw()

# 一行入力ボックスで名前を尋ねる --- (*1)
name = sd.askstring(
    '名前入力', 'お名前は？',
    initialvalue='くじら')

# 名前を使って挨拶 --- (*2)
mb.showinfo('挨拶', 'こんにちは,' + name + 'さん')
