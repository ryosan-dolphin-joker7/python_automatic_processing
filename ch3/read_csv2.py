import csv

# ファイルを開いてreaderを得る --- (*1)
with open('items2.csv', encoding='sjis') as f:
    reader = csv.reader(f)
    # ヘッダ行をスキップ --- (*2)
    head = next(reader)
    # 一行ずつ調べる --- (*3)
    total = 0
    for row in reader:
        # CSVの一行を変数に分ける --- (*4)
        name,price,cnt,subtotal = row
        print(name, price, cnt, subtotal)
        total += int(subtotal)
    # 合計を表示
    print("合計:", total, "円")

