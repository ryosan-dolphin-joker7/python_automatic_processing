import time, subprocess, platform
import pyautogui as pa

# 操作対象の画像(↓自分で作成したものを指定) --- (*1)
calc_png = 'calc.png'

# アプリのパスを指定 --- (*2)
if platform.system() == 'Windows':
    app = [r'c:\Windows\System32\calc.exe']
elif platform.system() == 'Darwin':
    app = ['open',
        '/System/Applications/Calculator.app']

# 電卓を起動 --- (*3)
subprocess.Popen(app)

# 電卓が起動するのを待機 --- (*4)
pos = None
for i in range(10):
    pos = pa.locateOnScreen(calc_png,
        grayscale=True, confidence=0.8)
    if pos is None:
        time.sleep(1)
        print('探しています')
        continue
    break
if pos is None:
    pa.alert('見つかりません')
    quit()
print('見つかりました:', pos)

# キーを送信して足し算を行う --- (*5)
if platform.system() == 'Windows':
    pa.write('2*3=', interval=0.3)
else:
    pa.write('6') # --- (*6)
print('キー送信完了') 
