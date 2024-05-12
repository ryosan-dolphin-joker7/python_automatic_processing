# リストの初期化
a_list = [0, 1, 22]

# 値を末尾に追加
a_list.append(3)
print( a_list ) # 結果→[0,1,22,3]

# リストを末尾に追加
a_list += [4, 5]
print( a_list ) # 結果→[0,1,22,3,4,5]

# 任意の部分を抜き出す
print( a_list[3:5] ) # 結果→[3,4]

# 要素数を調べる
print( len(a_list) ) # 結果→6

# リストの要素を削除
del a_list[2]
print( len(a_list) ) # 結果→5

