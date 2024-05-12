from selenium import webdriver
import time

# オプションを指定してChromeを起動 --- (*1)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# 作詞掲示板のユーザーページを開く --- (*2)
driver.get('https://uta.pw/sakusibbs/users.php?user_id=1')

# CSSクエリで作品一覧を取得 --- (*3)
a_list = driver.find_elements_by_css_selector(
        'ul#mmlist li a')
# 一覧を反復表示 --- (*4)
for a in a_list:
    print('■', a.text) # 作品名
    print('└', a.get_attribute('href')) # URL

# Chromeを閉じる --- (*5)
driver.close()
