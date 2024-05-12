# ダミーデータ
dummy_data = [
    ["伊藤", 300],
    ["伊藤", 600],
    ["伊藤", 200],
    ["田中", 300],
    ["田中", 200]
]

# データを顧客名で辞書型に分割 --- (*1)
users = {}
for row in dummy_data:
    name, value = row # 変数に分ける
    # 顧客名が初出ならリストを初期化 --- (*2)
    if name not in users:
        users[name] = []
    # 顧客名をキーに値にデータを追記 --- (*3)
    users[name].append(row)

# 顧客ごとに集計 --- (*4)
for name, rows in users.items():
    print(rows) # --- 集計対象データを表示
    # 顧客の購入金額を合計 --- (*5)
    total = 0
    for row in rows:
        total += row[1]
    print(name, total) # 結果を表示
