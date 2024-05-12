import PySimpleGUI as sg
from datetime import datetime

# 画面レイアウトを指定 --- (*1)
layout = [
    [sg.Text('デジタル時計')],
    [sg.Text('00:00:00',key='clock',font=('Helvetica', 72))]
]
# ウィンドウの作成
win = sg.Window('時計', layout)

# ウィンドウのイベントループ --- (*2)
while True:
    # イベントにおけるパラメーターの取得 --- (*3)
    event, val = win.read(timeout=100)
    # ウィンドウの終了イベントか?
    if event in ('Exit', 'Quit', None): break
    # 現在時刻のテキストを更新 --- (*4)
    s = datetime.now().strftime('%H:%M:%S')
    win['clock'].update(s)

# ウィンドウを閉じる
win.close()
