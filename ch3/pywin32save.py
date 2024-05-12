# pywin32(win32com)のライブラリを読み込み
import win32com.client as com
import os

# 保存先は絶対パスで指定する必要がある --- (*1)
scr_file = os.path.abspath(__file__)
scr_dir = os.path.dirname(scr_file)
save_file = scr_dir+'/pywin32save.xlsx'

# Excelを起動する --- (*2)
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# Excelに新規ワークブックを追加 --- (*3)
book = app.Workbooks.Add()
# アクティブなシートを得る
sheet = book.ActiveSheet

# シートに値を書き込む --- (*4)
sheet.Range("A1").Value = "すぐに怒らない人は優れた識別力がある"
sheet.Range("B2").Value = "心ない発言は剣のように突き刺す"
sheet.Range("C3").Value = "惜しみなく与える人は報われる"

# ブックを保存 --- (*5)
book.SaveAs(save_file)
# Exelを終了させる --- (*6)
app.Quit()
