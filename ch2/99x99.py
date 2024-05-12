import openpyxl as excel

# 新規ワークブックを作りワークシートを得る
book = excel.Workbook()
sheet = book.active

# 連続でセルに値を設定する --- (*1)
for y in range(1,100):
    for x in range(1,100):
        # セルを取得して値を設定 --- (*2)
        cell = sheet.cell(y, x)
        cell.value = x * y

# ファイルを保存
book.save("99x99.xlsx")

