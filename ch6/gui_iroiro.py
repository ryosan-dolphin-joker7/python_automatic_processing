import PySimpleGUI as sg
from datetime import datetime

# 画面レイアウトを指定 --- (*1)
layout = [
    [sg.Text('いろいろなGUI部品を使ってみよう！')],
    [sg.OK(), sg.Cancel()],
    [sg.Text('InputText:'), sg.InputText('あいうえお')],
    [sg.Text('Checkbox:'), sg.Checkbox('チェック')],
    [sg.Text('Radio:'), sg.Radio('ラジオ', group_id='r')],
    [sg.Text('Spin:'), sg.Spin([1,2,3,4,5])],
    [sg.Text('Listbox:'), sg.Listbox([1,2,3,4,5],size=(40,5))],
    [sg.Text('Slider:'), sg.Slider(range=(1,5),orientation='h')],
    [sg.Button('値を表示')]
]
# ウィンドウの作成
win = sg.Window('いろいろなGUI', layout)

# ウィンドウのイベントループ --- (*2)
while True:
    # イベントにおけるパラメーターの取得
    event, val = win.read()
    # ウィンドウの終了イベントか?
    if event in ('Exit', 'Quit', None): break
    if event == '値を表示':
        print(event, val)

# ウィンドウを閉じる
win.close()
