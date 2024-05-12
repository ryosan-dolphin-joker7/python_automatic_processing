import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd

# tkinterの窓を表示しない
tk.Tk().withdraw()
# ファイル選択ダイアログを出す --- (*1)
filepath = fd.askopenfilename()
# 結果を表示 --- (*2)
mb.showinfo('対象ファイル', filepath)
