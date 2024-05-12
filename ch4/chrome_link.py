from selenium import webdriver
import time

driver = webdriver.Chrome()

# 作詞掲示板のトップページを開く --- (*1)
driver.get('https://uta.pw/sakusibbs/')

# 名作アーカイブというリンクを探す --- (*2)
link = driver.find_element_by_link_text('名作アーカイブ')
# 見つけたリンクをクリック --- (*3)
link.click()

time.sleep(30) # 30秒後に閉じる
driver.close()
