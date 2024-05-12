import win32com.client as com
import os

# ファイルは絶対パスで指定する必要がある --- (*1)
scr_file = os.path.abspath(__file__)
scr_dir = os.path.dirname(scr_file)
in_file = scr_dir+'/date-sample.xlsx'
pdf_file = scr_dir+'/date-sample.pdf'

# Excelを起動する --- (*2)
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# Excelでブックを読み込む --- (*3)
book = app.Workbooks.Open(in_file)

# ブックをPDFでエクスポート --- (*4)
xlTypePDF = 0 # PDFを表す定数
book.ExportAsFixedFormat(xlTypePDF, pdf_file)

# Exelを終了させる --- (*5)
app.Quit()
