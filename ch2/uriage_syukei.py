import openpyxl as excel

# 売上データのブックを開いてシートを取り出す
book = excel.load_workbook(
    "uriage.xlsx", data_only=True)
sheet = book.active

# 購入者を辞書データに入れていく --- (*1)
name_dic = {} 
# A3からF999(データの適当な範囲)を取り出す --- (*2)
rows = sheet["A3":"F999"]
for row in rows:
    # セルの値をリストとして得る
    values = [cell.value for cell in row]
    # 無効な行やデータを飛ばす --- (*3)
    if values[0] is None: break
    # 購入者をキーにして辞書データに追記 --- (*4)
    name = values[1]
    if name not in name_dic:
        name_dic[name] = []
    name_dic[name].append(values)
    
# 購入者ごとに集計して表示 --- (*5)
for name in name_dic.keys():
    total = 0
    for row in name_dic[name]:
        # 各データを変数に代入 --- (*6)
        date = row[0] # 日付
        goods_name = row[2] # 商品名
        num = row[3] # 個数
        price = row[4] # 値段
        subtotal = row[5] # 小計
        total += subtotal
    # 集計結果を表示 --- (*7)
    print(name+"様> 請求金額:", total, "円")
