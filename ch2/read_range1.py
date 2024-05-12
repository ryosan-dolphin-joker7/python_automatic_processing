import openpyxl as excel

# ワークブックを開いてシートを得る --- (*1)
book = excel.load_workbook("test100.xlsx")
sheet = book.active

# 連続でセルの値を得て表示 --- (*2)
for y in range(2, 5):
    r = []
    for x in range(2, 5):
        v = sheet.cell(row=y, column=x).value
        r.append(v)
    print(r)
