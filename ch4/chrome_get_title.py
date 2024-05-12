from selenium import webdriver

driver = webdriver.Chrome()

# 作詞掲示板の作品ページを開く --- (*1)
url = 'https://uta.pw/sakusibbs/post.php?mml_id=35'
driver.get(url)
# class属性がposttitleの要素を取得 --- (*2)
e = driver.find_element_by_class_name('posttitle')
# 取得したテキスト表示 --- (*3)
print(e.text)

driver.close()
