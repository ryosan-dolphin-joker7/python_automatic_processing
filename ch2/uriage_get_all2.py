import openpyxl as excel

# 売上データのブックを開いてシートを取り出す
book = excel.load_workbook("uriage.xlsx")
sheet = book.active

# A3からF9のセルを取り出す --- (*1)
rows = sheet["A3":"F9"]
for row in rows:
    # セルの値をリストとして得る --- (*2)
    values = []
    for cell in row:
        values.append(cell.value)
    # リストを表示する --- (*3)
    print(values)
