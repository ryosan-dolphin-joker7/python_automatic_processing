import kdialog as kd
# 一行入力ダイアログ --- (*1)
name = kd.input('お名前は?')
# 二択ダイアログ --- (*2)
if not kd.yesno(name+'さん、実行しますか?'):
    kd.info('中止しました')
    quit()
# ファイル選択ダイアログ --- (*3)
kd.info('対象ファイルを選んでください。')
fname = kd.select_file()
kd.info('選択:' + fname)
