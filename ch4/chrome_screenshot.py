from selenium import webdriver

# Chromeを起動する
driver = webdriver.Chrome()
# Pythonのページを開く
driver.get('https://python.org')
# スクリーンショット撮影
driver.save_screenshot('screenshot.png')
driver.quit()
