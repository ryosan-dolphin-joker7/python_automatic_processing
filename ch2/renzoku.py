import openpyxl as excel

# 新規ワークブックを作る --- (*1)
book = excel.Workbook()
# アクティブなワークシートを得る --- (*2)
sheet = book.active

# 連続でセルに値を設定する --- (*3)
for i in range(10):
    # セルに値を設定 --- (*4)
    sheet.cell(row=(i+1), column=1, value=i)

# ファイルを保存 --- (*5)
book.save("renzoku.xlsx")
