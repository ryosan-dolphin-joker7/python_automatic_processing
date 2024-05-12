import PySimpleGUI as sg
import sys, os

# リソースフォルダにアクセスする関数 --- (*1)
def get_resource(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return filename

# 画面レイアウトを指定してウィンドウを作成 --- (*2)
layout = [
    [sg.Text('リソースから画像を表示')],
    [sg.Image(get_resource('res/data.png'))]
]
win = sg.Window('リソースを使うサンプル', layout)

# ウィンドウのイベントループ --- (*3)
while True:
    # イベントにおけるパラメーターの取得
    event, val = win.read()
    # ウィンドウの終了イベントか?
    if event in ('Exit', 'Quit', None): break
win.close()

