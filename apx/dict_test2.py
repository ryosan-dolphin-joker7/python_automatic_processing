# 辞書型の初期化
a_dict = {'apple': 280, 'banana': 150, 'orange': 220}

# キーが含まれているか
print( 'banana' in a_dict ) # 結果→True
print( 'mango' in a_dict ) # 結果→False

# キーの一覧を取得
print( a_dict.keys() ) 
# 結果→dict_keys(['apple', 'banana', 'orange'])

# 辞書型に別の辞書型を追加
a_dict.update({'grape': 900, 'pear': 450})
print(a_dict['grape']) # 結果→900

# 辞書型から値を削除
del a_dict['banana']
print( 'banana' in a_dict ) # 結果→False
