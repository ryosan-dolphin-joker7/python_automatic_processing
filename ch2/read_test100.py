import openpyxl as excel

# ワークブックを開く
book = excel.load_workbook("test100.xlsx")
# ワークシートを取り出す
sheet = book.active

# H2のセルの値を得る --- (*1)
print( sheet["H2"].value )

# H2のセルの値を得る --- (*2)
cell = sheet.cell(row=2, column=8)
print( cell.value )
