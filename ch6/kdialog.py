# 簡単に使えるダイアログをまとめたモジュール
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
import tkinter.simpledialog as sd

# tkinterの窓を表示しない
tk.Tk().withdraw()

# メッセージボックスを表示
def info(message, title='情報'):
    mb.showinfo(title, message)

# 警告ダイアログを表示
def warning(message, title='情報'):
    mb.showwarning(title, message)

# はい・いいえの二択ダイアログを表示
def yesno(message, title='質問'):
    return mb.askyesno(title, message)

# 一行入力ボックスを表示
def input(message, title='質問', value=''):
    return sd.askstring(
        title, message,
        initialvalue=value)

# ファイルの選択ダイアログ
def select_file(initdir='./'):
    return fd.askopenfilename(
        initialdir=initdir)

# ファイル保存ダイアログ
def select_savefile(initdir='./'):
    return fd.asksaveasfilename(
        initialdir=initdir)

# フォルダ選択ダイアログ
def select_dir(initdir='./'):
    return fd.askdirectory(
        initialdir=initdir)
