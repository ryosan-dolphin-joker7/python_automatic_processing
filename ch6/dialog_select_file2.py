import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd

# tkinterの窓を表示しない
tk.Tk().withdraw()

# 初期ディレクトリを指定してファイル選択 --- (*1)
filepath = fd.askopenfilename(
    filetypes=[('Pythonファイル','*.py')],
    initialdir='./')

# 結果を表示
mb.showinfo('対象ファイル', filepath)
