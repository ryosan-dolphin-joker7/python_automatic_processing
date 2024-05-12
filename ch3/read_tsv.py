import csv

# ファイルを開く --- (*1)
with open('items3.tsv', encoding='utf-8') as f:
    # 区切り記号を指定して読み込む --- (*2)
    reader = csv.reader(f, delimiter='\t')
    # 読んだデータを画面に表示
    for row in reader:
        print(row)

