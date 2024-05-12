from datetime import datetime

# 就寝時間と起床時刻を指定 --- (*1)
sleep_t  = datetime(2023, 1, 1,22, 0, 0)
wakeup_t = datetime(2023, 1, 2, 8,30, 0)
# 時間計算 --- (*2)
delta = wakeup_t - sleep_t
print(type(delta))
sec = delta.seconds # あと何秒か?
hours = sec / (60 * 60)
# 結果を表示 --- (*3)
print('あと'+str(hours)+'時間です')

