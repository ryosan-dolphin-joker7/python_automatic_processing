import os

# 作業フォルダから対象ファイルの絶対パスを得る --- (*1)
path1 = os.path.abspath('./name1.xlsx')
print(path1)

# プログラム自身から対象ファイルの絶対パスを得る --- (*2)
base_dir = os.path.dirname(__file__)
path2 = os.path.join(base_dir, 'name1.xlsx')
path2 = os.path.abspath(path2)
print(path2)



