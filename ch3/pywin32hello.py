# pywin32(win32com)のライブラリを読み込み --- (*1)
import win32com.client as com

# Excelを起動する --- (*2)
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# Excelに新規ワークブックを追加 --- (*3)
book = app.Workbooks.Add()
# アクティブなシートを得る --- (*4)
sheet = book.ActiveSheet

# シートに値を書き込む --- (*5)
sheet.Range("B2").Value = "こんにちは"
