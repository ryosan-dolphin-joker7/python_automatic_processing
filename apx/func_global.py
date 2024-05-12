# 名前を設定する関数
def set_name(new_name):
    global name
    name = new_name

# 挨拶をする関数
def say_hello():
    global name
    print('こんにちは', name, 'さん!')

# 関数を使う
set_name('クジラ')
say_hello()

# 表示結果→ こんにちは クジラ さん!


