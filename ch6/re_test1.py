import re

# 正規表現で検索
target = r'app dog art pot'
pattern = r'a..'
a = re.findall(pattern, target)

# 結果を出力
print(a)
