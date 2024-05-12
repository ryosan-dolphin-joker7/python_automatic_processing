import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd

# tkinterの窓を表示しない
tk.Tk().withdraw()

# フォルダの選択 --- (*1)
dirpath = fd.askdirectory(
    title='実行するフォルダを指定してください',
    initialdir='./')

# 結果を表示
mb.showinfo('対象フォルダ', dirpath)
