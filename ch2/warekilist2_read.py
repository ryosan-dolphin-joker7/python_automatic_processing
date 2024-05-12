import openpyxl as excel

# 新規ワークブックを作ってシートを得る
book = excel.load_workbook(
    "wareki2.xlsx", data_only=True)
sheet = book.active

# 任意の範囲を読む
rows = sheet["A1:B101"]
for row in rows:
    values = [v.value for v in row]
    print(values)


