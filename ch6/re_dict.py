import re

# 辞書ファイルのパス
dict_file = './ejdict-hand-utf8.txt'

# 繰り返し処理を行う --- (*1)
while True:
    # 正規表現を入力してもらう --- (*2)
    print('正規表現を入力してください。[q]で終了。')
    re_str = input()
    if re_str == '': continue
    if re_str == 'q': break
    # 英和辞書から正規表現に対応する単語を探す --- (*3)
    with open(dict_file, 'rt', encoding='utf-8') as f:
        cnt = 0
        while True:
            # 一行だけ読む
            line = f.readline()
            if not line: break
            # 英単語を得る
            word, mean = line.split('\t')
            # 正規表現マッチ --- (*4)
            if re.search(re_str, word):
                print(word) # 該当すれば表示
                cnt += 1
                if cnt > 50: break # 最大50件
