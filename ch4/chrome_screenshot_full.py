from selenium import webdriver

# キャプチャしたいページのURL
url = 'https://python.org'
# 保存先
save_file = 'screenshot_full.png'

# メイン処理 --- (*1)
def screenshot_full(url, save_file):
    # 最初にページサイズを取得
    w, h = get_page_size(url)
    # 指定サイズでChromeを起動し画面をキャプチャ
    screenshot_size(url, save_file, w, h)

# ページの幅と高さを取得する --- (*2)
def get_page_size(url):
    # ブラウザを起動してURLを開く
    driver = webdriver.Chrome()
    driver.get(url)
    # ページ幅を取得 (JavaScriptを実行する) --- (*3)
    w = driver.execute_script(
        "return document.body.scrollWidth;")
    h =  driver.execute_script(
        "return document.body.scrollHeight;")
    driver.close() # サイズを得たら閉じる
    print('page_size=', w, h)
    return (w, h)

# 指定サイズでページを保存 --- (*4)
def screenshot_size(url, save_file, w, h):
    # 指定画面サイズで改めてChromeを起動する --- (*5)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # 画面サイズを指定
    win_size = 'window-size='+str(w)+','+str(h)
    options.add_argument(win_size)
    # Chromeを起動しページを開いてキャプチャ --- (*6)
    cap_driver = webdriver.Chrome(options=options)
    cap_driver.get(url)
    cap_driver.save_screenshot(save_file)
    cap_driver.close()

if __name__ == '__main__':
    screenshot_full(url, save_file)
