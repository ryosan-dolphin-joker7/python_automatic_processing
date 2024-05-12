import tkinter as tk
import tkinter.messagebox as mb

# tkinterのウィンドウを隠す --- (*1)
tk.Tk().withdraw()

# メッセージを表示 --- (*2)
mb.showinfo("ことわざ", "二度あることは三度ある")

