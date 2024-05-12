# SeleniumのWebDriverを取り込む --- (*1)
from selenium import webdriver
import time

# Chromeを起動する --- (*2)
driver = webdriver.Chrome()
# Pythonのページを開く --- (*3)
driver.get('https://python.org')
# 30秒後に終了する --- (*4)
time.sleep(30)
driver.quit()
