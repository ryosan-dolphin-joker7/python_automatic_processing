import csv, openpyxl as excel
# 設定
in_file = 'meibo.csv'
template_file = 'card-template.xlsx'
save_file = 'card-meibo.xlsx'

# CSVファイルを読み込む --- (*1)
def read_csv(fname):
    with open(fname, encoding='sjis') as f:
        reader = csv.reader(f)
        next(reader) # ヘッダを読み飛ばす
        return [v for v in reader]

# Excelブックを読み込む --- (*2)
book = excel.load_workbook(template_file)
# テンプレートのシートを得る --- (*3)
sheet_tpl = book['Sheet']
# CSVから顧客一覧を得て一人ずつ処理 --- (*4)
for i, person in enumerate(read_csv(in_file)):
    # CSVの一行を変数に割り振る
    name, zipno, addr = person
    # 1枚のページに10枚ずつ --- (*5)
    idx = i % 10
    if idx == 0:
        # テンプレートのシートをコピー --- (*6)
        sheet = book.copy_worksheet(sheet_tpl)
        sheet.title = 'Page'+str(idx)
    # 書き込むセル位置を決定 --- (*7)
    row = 4 * (idx % 5) + 2
    col = 2 * (idx // 5) + 2
    # セルにデータを書き込む
    sheet.cell(row=row+0, column=col, value=name)
    sheet.cell(row=row+1, column=col, value=zipno)
    sheet.cell(row=row+2, column=col, value=addr)
# テンプレートのシートを削除して保存 --- (*8)
book.remove(sheet_tpl)
book.save(save_file)
