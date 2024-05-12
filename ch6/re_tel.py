import re
# 対象文字列
tel = r'[電話] 000-1111-2222'
# 検索パターン
pattern = r'(\d+)-(\d+)-(\d+)'
# 置換後
rep = r'(\1) \2 - \3'
print(re.sub(pattern, rep, tel))
