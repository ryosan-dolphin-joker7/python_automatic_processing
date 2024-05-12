import openpyxl as excel

# ワークブック(Excelファイル)を開く --- (*1)
book = excel.load_workbook("hello.xlsx")

# 先頭のワークシートを取り出す --- (*2)
sheet = book.worksheets[0]

# A1のセルの値を得る --- (*3)
cell = sheet["A1"]

# 読み出した結果を画面に出力 --- (*4)
print(cell.value)
