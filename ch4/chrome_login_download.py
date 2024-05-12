from selenium import webdriver
import os, time

# 作詞掲示板のログインの情報を指定 --- (*1)
login_url = 'https://uta.pw/sakusibbs/users.php?action=login'
user_id, password = ('JS-TESTER', 'ipCU12ySxI')
# 保存先フォルダ(絶対パスで指定) --- (*2)
save_dir = os.path.dirname(os.path.abspath(__file__))
save_file = save_dir + '/list.csv'
# Chromeのオプションで保存先フォルダを設定 --- (*3)
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'download.default_directory': save_dir})

# メイン処理 --- (*4)
def login_download():
    # Chromeを起動 --- (*5)
    driver = webdriver.Chrome(options=options)
    # ログイン処理実行 --- (*6)
    try_login(driver)
    # マイページに行く --- (*7)
    link_click(driver, 'マイページ')
    # ダウンロード --- (*8)
    link_click(driver, 'CSVでダウンロード')
    # ダウンロード完了まで最大30秒待機 --- (*9)
    for i in range(30):
        if os.path.exists(save_file): break
        time.sleep(1)

# ログイン処理 --- (*10)
def try_login(driver):
    # ログインページを開く --- (*11)
    driver.get(login_url)
    # ユーザー名とパスワードを書き込む --- (*12)
    usr = driver.find_element_by_name('username_mmlbbs6')
    usr.send_keys(user_id)
    pwd = driver.find_element_by_name('password_mmlbbs6')
    pwd.send_keys(password)
    pwd.submit() # 送信 

# ラベルを指定してリンクを検索しクリックする --- (*13)
def link_click(driver, label):
    a = driver.find_element_by_partial_link_text(label)
    a.click()

if __name__ == '__main__':
    login_download()
