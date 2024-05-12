from selenium import webdriver
import time

driver = webdriver.Chrome()

# Googleトップページを開く --- (*1)
driver.get('https://google.com')

# 検索ボックスを探す --- (*2)
el = driver.find_element_by_name('q')
# キーワードを入力 --- (*3)
el.send_keys('Pythonの教科書')
# フォームを送信する --- (*4)
el.submit()

time.sleep(30) # 30秒後に閉じる
driver.close()
