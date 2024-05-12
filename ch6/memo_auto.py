import time, subprocess, platform
import pyautogui as pa

# Windowsでメモ帳を起動 --- (*1)
if platform.system() == 'Windows':
    subprocess.Popen(r'c:\Windows\notepad.exe')
    time.sleep(2) # 起動待機 --- (*2)

# macOSでテキストエディットを起動 --- (*3)
if platform.system() == 'Darwin':
    subprocess.Popen(['open',
        '/System/Applications/TextEdit.app'])
    time.sleep(2) # 起動待機 --- (*4)
    pa.hotkey('command', 'n') # 新規書類 --- (*5)
    time.sleep(2)

# 文字を入力 --- (*6)
pa.write('Hello, Python!')
