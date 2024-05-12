import time
import pyautogui as pa

pa.alert('この後5秒以内にペイントツールをアクティブにしてください。')
time.sleep(5)

# 描画開始座標を指定 --- (*1)
bx = 400
by = 400

# マウス操作 --- (*2)
pa.moveTo(bx, by) # 任意の位置に移動
pa.dragTo(bx+300, by+300, 2, button='left') # 2秒かけてドラッグ
pa.drag(-300,0, 2, button='left') # 相対座標を指定してドラッグ
pa.drag(0,-300, 2, button='left') # 相対座標を指定してドラッグ

# 繰り返しマウス操作 --- (*3)
sec = 0.1
for i in range(5):
    d = i * 10 + 10
    pa.moveTo(bx+d, bx+d)
    pa.drag(0, 300+d, sec, button='left')
    pa.drag(300+d, 0, sec, button='left')
    pa.drag(0, -300-d, sec, button='left')
    pa.drag(-300-d, 0, sec, button='left')
