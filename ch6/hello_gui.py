import PySimpleGUI as sg

# 画面レイアウトを指定 --- (*1)
layout = [
    [sg.Text('こんにちは！')],
    [sg.Text('簡単にGUIが作れます！')],
    [sg.OK()],
]
# ウィンドウの作成 --- (*2)
win = sg.Window('サンプル', layout)

# ウィンドウのイベントループ --- (*3)
while True:
    # イベントにおけるパラメーターの取得 --- (*4)
    event, val = win.read()
    # ウィンドウの終了イベントか?
    if event in ('Exit', 'Quit', None): break
    # OKボタンが押された?
    if event == 'OK': break

# ウィンドウを閉じる --- (*5)
win.close()

