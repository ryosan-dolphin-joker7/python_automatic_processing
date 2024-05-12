import PySimpleGUI as sg

# 画面レイアウトを指定 --- (*1)
layout = [
    [sg.Text('インチをセンチメートルに変換します。')],
    [sg.Text('インチ'), sg.InputText(key='inch')],
    [sg.Button('変換')],
    [sg.Text('---', key='info', size=(40,1))]
]
# ウィンドウの作成
win = sg.Window('インチ→センチ変換', layout)

# ウィンドウのイベントループ --- (*2)
while True:
    # イベントにおけるパラメーターの取得 --- (*3)
    event, val = win.read()
    # ウィンドウの終了イベントか?
    if event in ('Exit', 'Quit', None): break
    # 変換ボタンが押された? --- (*4)
    if event == '変換':
        inch = float(val['inch'])
        cm = inch * 2.54
        s = '{0}inch = {1}cm'.format(inch, cm)
        # テキストを更新 --- (*5)
        win['info'].update(s)

# ウィンドウを閉じる
win.close()
