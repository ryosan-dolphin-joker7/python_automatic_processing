from datetime import datetime

# 予定日を指定 --- (*1)
yoteibi = datetime(2025, 4, 13)
# 今日を指定 --- (*2)
now = datetime.now()
# 日付計算 --- (*3)
delta = yoteibi - now
# 結果を表示 --- (*4)
print('あと'+str(delta.days+1)+'日です')

