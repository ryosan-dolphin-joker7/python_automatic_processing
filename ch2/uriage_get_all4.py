import openpyxl as excel

# 売上データのブックを開いてシートを取り出す
book = excel.load_workbook(
    "uriage.xlsx", data_only=True)
sheet = book.active

# A3からF999(データの適当な範囲)を取り出す --- (*1)
rows = sheet["A3":"F999"]
for row in rows:
    # セルの値をリストとして得る --- (*2)
    values = [cell.value for cell in row]
    # 空白セルであれば読み取りを終わる --- (*3)
    if values[0] is None: break
    # リストを表示する
    print(values)
